import pandas as pd


#Laden der Daten
def lade_aktivitaets_daten(dateipfad):
    try:
        df = pd.read_csv(dateipfad)
        return df 
            
    except FileNotFoundError:
        print(f"Fehler: Die Datei unter '{dateipfad}' wurde nicht gefunden.")
        return None


#Validierung der Daten
def validate_data(df):
    benoetigte_spalten = ["PowerOriginal", "Duration"]
    fehlende = [s for s in benoetigte_spalten if s not in df.columns]
    if fehlende:
        print(f"Fehler: Fehlende Spalten: {', '.join(fehlende)}")
        return None

    if len(df) == 0:
        print("Fehler: Die Datei enthält keine Daten.")
        return None

    vorher = len(df)
    df = df.dropna(subset=["PowerOriginal", "Duration"])
    entfernt = vorher - len(df)
    if entfernt > 0:
        print(f"Hinweis: {entfernt} Zeilen mit fehlenden Werten entfernt.")

    if len(df) == 0:
        print("Fehler: Nach Bereinigung keine Daten mehr übrig.")
        return None

    if df["PowerOriginal"].eq(0).all():
        print("Fehler: 'PowerOriginal' enthält nur Nullen.")
        return None

    if (df["Duration"] <= 0).any():
        print("Fehler: 'Duration' enthält ungültige Werte (≤ 0).")
        return None

    return df