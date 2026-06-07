import os
from read_data import lade_aktivitaets_daten, validate_data
from power_curve import calculate_power_curve, plot_power_curve, save_power_curve


#Pfad zur Datenquelle
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_PATH = os.path.join(BASE_DIR, "..", "Data", "activity.csv")


def main():
    df = lade_aktivitaets_daten(DATA_PATH)

    if df is not None:
        df = validate_data(df)

    if df is None:
        return

    result = calculate_power_curve(df["PowerOriginal"], df["Duration"])
    print("\nPower Curve Ergebnisse:")
    print(result.to_string(index=False))

    fig = plot_power_curve(result)
    save_power_curve(fig)
    fig.show()


if __name__ == "__main__":
    main()

