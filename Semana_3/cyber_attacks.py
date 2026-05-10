import re

import pandas as pd

CSV_PATH = "cybersecurity_attacks.csv"
CLEANED_CSV_PATH = "cybersecurity_attacks_cleaned.csv"

IPV4_PATTERN = re.compile(
    r"^(25[0-5]|2[0-4]\d|1\d{2}|[1-9]?\d)\.(25[0-5]|2[0-4]\d|1\d{2}|[1-9]?\d)\.(25[0-5]|2[0-4]\d|1\d{2}|[1-9]?\d)\.(25[0-5]|2[0-4]\d|1\d{2}|[1-9]?\d)$"
)


def is_valid_ipv4(ip_address: str) -> bool:
    if not isinstance(ip_address, str):
        return False
    return bool(IPV4_PATTERN.match(ip_address.strip()))


def clean_dataframe(df: pd.DataFrame) -> pd.DataFrame:
    original_count = len(df)
    df = df.drop_duplicates()

    df["Timestamp"] = pd.to_datetime(df["Timestamp"], errors="coerce")
    df = df[df["Timestamp"].notna()]

    valid_ip_source = df["Source IP Address"].apply(is_valid_ipv4)
    valid_ip_dest = df["Destination IP Address"].apply(is_valid_ipv4)
    df = df[valid_ip_source & valid_ip_dest]

    valid_ports = df["Source Port"].between(1, 65535) & df["Destination Port"].between(1, 65535)
    df = df[valid_ports]

    df = df[df["Packet Length"].between(1, 10000)]

    text_columns = [
        col for col in df.columns if df[col].dtype == object and col != "Timestamp"
    ]
    for col in text_columns:
        if col == "Payload Data":
            df[col] = df[col].fillna("")
        elif col in ["Malware Indicators", "Alerts/Warnings", "Proxy Information", "Firewall Logs", "IDS/IPS Alerts"]:
            df[col] = df[col].fillna("None")
        else:
            df[col] = df[col].fillna("Unknown")

    numeric_columns = [col for col in df.columns if df[col].dtype.kind in "if"]
    for col in numeric_columns:
        df[col] = df[col].fillna(0)

    df = df.reset_index(drop=True)
    cleaned_count = len(df)

    print(f"=== Limpeza do dataset ===")
    print(f"Registros originais: {original_count}")
    print(f"Registros após limpeza: {cleaned_count}")
    print(f"Registros removidos: {original_count - cleaned_count}\n")

    return df


def main() -> None:
    df = pd.read_csv(CSV_PATH)

    df = clean_dataframe(df)
    df.to_csv(CLEANED_CSV_PATH, index=False)

    print("=== Primeiras linhas ===")
    print(df.head(10).to_string(index=False), end="\n\n")

    print("=== Informações do DataFrame ===")
    df.info()
    print("\n")

    print("=== Estatísticas descritivas ===")
    print(df.describe(include="all").transpose())


if __name__ == "__main__":
    main()
