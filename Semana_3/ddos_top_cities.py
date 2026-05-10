import pandas as pd

CSV_PATH = "cybersecurity_attacks.csv"


def main() -> None:
    df = pd.read_csv(CSV_PATH)

    df["Timestamp"] = pd.to_datetime(df["Timestamp"], errors="coerce")
    df = df[df["Timestamp"].notna()]

    latest_date = df["Timestamp"].max()
    one_month_before = latest_date - pd.DateOffset(months=1)

    df = df[df["Timestamp"] >= one_month_before]
    df = df[df["Attack Type"].astype(str).str.contains("DDoS", case=False, na=False)]

    if df.empty:
        print("Nenhum ataque DDoS encontrado no último mês do dataset.")
        return

    df["City"] = (
        df["Geo-location Data"].astype(str)
        .str.split(",", n=1)
        .str[0]
        .str.strip()
        .replace({"nan": "Unknown", "": "Unknown"})
    )

    # Calcular duração média entre ataques por cidade
    df = df.sort_values(["City", "Timestamp"])
    df["Time Diff"] = df.groupby("City")["Timestamp"].diff().dt.total_seconds()
    avg_duration_per_city = (
        df.groupby("City")["Time Diff"]
        .mean()
        .dropna()
        .sort_values(ascending=False)
        .reset_index(name="Avg Duration (seconds)")
    )

    top_cities = (
        df.groupby("City")
        .size()
        .sort_values(ascending=False)
        .head(10)
        .reset_index(name="Attack Count")
    )

    print(f"Último mês usado no dataset: {one_month_before.date()} até {latest_date.date()}")
    print("\nTop 10 cidades com mais ataques DDoS:")
    print(top_cities.to_string(index=False))

    print("\nMédia de duração entre ataques consecutivos por cidade (top 10 por contagem):")
    merged = top_cities.merge(avg_duration_per_city, on="City", how="left")
    print(merged.to_string(index=False))


if __name__ == "__main__":
    main()
