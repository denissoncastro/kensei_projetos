import matplotlib.pyplot as plt
import pandas as pd

CSV_PATH = "cybersecurity_attacks.csv"
DASHBOARD_PNG = "ddos_top_cities_dashboard.png"


def load_and_filter_data() -> pd.DataFrame:
    df = pd.read_csv(CSV_PATH)
    df["Timestamp"] = pd.to_datetime(df["Timestamp"], errors="coerce")
    df = df[df["Timestamp"].notna()]

    latest_date = df["Timestamp"].max()
    one_month_before = latest_date - pd.DateOffset(months=1)

    df = df[df["Timestamp"] >= one_month_before]
    df = df[df["Attack Type"].astype(str).str.contains("DDoS", case=False, na=False)]

    df["City"] = (
        df["Geo-location Data"].astype(str)
        .str.split(",", n=1)
        .str[0]
        .str.strip()
        .replace({"nan": "Unknown", "": "Unknown"})
    )

    return df, latest_date, one_month_before


def build_dashboard(df: pd.DataFrame, latest_date: pd.Timestamp, one_month_before: pd.Timestamp) -> None:
    counts = df["City"].value_counts().head(10)
    top3 = counts.head(3)

    avg_durations = (
        df.sort_values(["City", "Timestamp"])
        .groupby("City")["Timestamp"]
        .apply(lambda group: group.diff().dt.total_seconds().mean())
        .dropna()
    )

    top3_summary = pd.DataFrame({
        "Attack Count": top3,
        "Avg Interval (hours)": (avg_durations[top3.index] / 3600).round(2),
    }).reset_index().rename(columns={"index": "City"})

    fig, axes = plt.subplots(3, 1, figsize=(12, 18), constrained_layout=True)

    colors = ["tomato" if city in top3.index else "steelblue" for city in counts.index]
    counts.plot(
        kind="bar",
        ax=axes[0],
        color=colors,
        edgecolor="black",
    )
    axes[0].set_title("Top 10 Cidades com Mais Ataques DDoS no Último Mês", fontsize=16)
    axes[0].set_xlabel("Cidade")
    axes[0].set_ylabel("Número de Ataques")
    axes[0].tick_params(axis="x", rotation=45)

    axes[1].bar(top3.index, top3.values, color=["tomato", "orangered", "darkred"], edgecolor="black")
    axes[1].set_title("Três Cidades Mais Atacadas", fontsize=16)
    axes[1].set_xlabel("Cidade")
    axes[1].set_ylabel("Ataques DDoS")
    axes[1].tick_params(axis="x", rotation=45)

    axes[2].axis("off")
    table = axes[2].table(
        cellText=top3_summary.values,
        colLabels=top3_summary.columns,
        cellLoc="center",
        loc="center",
    )
    table.auto_set_font_size(False)
    table.set_fontsize(12)
    table.scale(1, 2)
    axes[2].set_title("Resumo das 3 Cidades Mais Atacadas", fontsize=16, pad=20)

    fig.suptitle(
        f"Dashboard de Ataques DDoS ({one_month_before.date()} a {latest_date.date()})",
        fontsize=20,
        y=1.02,
    )

    fig.savefig(DASHBOARD_PNG, dpi=150, bbox_inches="tight")
    plt.close(fig)

    print(f"Dashboard salvo em {DASHBOARD_PNG}")


def main() -> None:
    df, latest_date, one_month_before = load_and_filter_data()
    if df.empty:
        print("Nenhum ataque DDoS encontrado no último mês do dataset.")
        return

    build_dashboard(df, latest_date, one_month_before)


if __name__ == "__main__":
    main()
