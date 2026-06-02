import pandas as pd

def lade_aktivitaets_daten(dateipfad):
    """
    Lädt eine CSV-Datei und gibt die Watt-Spalte zurück.
    """
    try:
        # CSV-Datei einlesen
        # Falls deine Datei Semikolons nutzt, füge sep=';' hinzu
        df = pd.read_csv(dateipfad)
        return df 
            
    except FileNotFoundError:
        print(f"Fehler: Die Datei unter '{dateipfad}' wurde nicht gefunden.")
        return None

if __name__ == "__main__":
    lade_aktivitaets_daten("data/activity.csv")
