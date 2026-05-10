import matplotlib.pyplot as plt
import pandas as pd

CSV_PATH = "cybersecurity_attacks.csv"


def create_bar_chart_top_cities(df):
    """Gráfico de barras: Top 10 cidades com mais ataques DDoS no último mês."""
    df["Timestamp"] = pd.to_datetime(df["Timestamp"], errors="coerce")
    df = df[df["Timestamp"].notna()]

    latest_date = df["Timestamp"].max()
    one_month_before = latest_date - pd.DateOffset(months=1)

    df_filtered = df[df["Timestamp"] >= one_month_before]
    df_filtered = df_filtered[df_filtered["Attack Type"].astype(str).str.contains("DDoS", case=False, na=False)]

    df_filtered["City"] = (
        df_filtered["Geo-location Data"].astype(str)
        .str.split(",", n=1)
        .str[0]
        .str.strip()
        .replace({"nan": "Unknown", "": "Unknown"})
    )

    top_cities = (
        df_filtered.groupby("City")
        .size()
        .sort_values(ascending=False)
        .head(10)
    )

    plt.figure(figsize=(10, 6))
    top_cities.plot(kind='bar', color='skyblue')
    plt.title('Top 10 Cidades com Mais Ataques DDoS (Último Mês)')
    plt.xlabel('Cidade')
    plt.ylabel('Número de Ataques')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.savefig('top_cities_bar.png')
    plt.close()


def create_line_chart_attacks_per_month(df):
    """Gráfico de linha: Ataques por mês."""
    df["Timestamp"] = pd.to_datetime(df["Timestamp"], errors="coerce")
    df = df[df["Timestamp"].notna()]

    df["Month"] = df["Timestamp"].dt.to_period('M')
    attacks_per_month = df.groupby("Month").size()

    plt.figure(figsize=(10, 6))
    attacks_per_month.plot(kind='line', marker='o', color='red')
    plt.title('Ataques por Mês')
    plt.xlabel('Mês')
    plt.ylabel('Número de Ataques')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig('attacks_per_month_line.png')
    plt.close()


def create_pie_chart_attack_types(df):
    """Gráfico de pizza: Tipos de ataque."""
    attack_types = df["Attack Type"].value_counts()

    plt.figure(figsize=(8, 8))
    attack_types.plot(kind='pie', autopct='%1.1f%%', startangle=140, colors=plt.cm.Paired.colors)
    plt.title('Distribuição dos Tipos de Ataque')
    plt.ylabel('')
    plt.tight_layout()
    plt.savefig('attack_types_pie.png')
    plt.close()


def main():
    df = pd.read_csv(CSV_PATH)

    create_bar_chart_top_cities(df)
    create_line_chart_attacks_per_month(df)
    create_pie_chart_attack_types(df)

    print("Gráficos salvos como PNG:")
    print("- top_cities_bar.png")
    print("- attacks_per_month_line.png")
    print("- attack_types_pie.png")


if __name__ == "__main__":
    main()
