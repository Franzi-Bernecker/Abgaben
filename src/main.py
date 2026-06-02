import pandas as pd

def main():
    # 1. Pfad zur Datei definieren
    # Da die Datei im selben Ordner wie main.py liegt, reicht der Name
    dateiname = "activity.csv"
    
    try:
        # 2. Die CSV-Datei in einen sogenannten "DataFrame" laden
        # (Ein DataFrame ist wie eine Excel-Tabelle in Python)
        df = pd.read_csv(dateiname)
        
        print("Erfolgreich geladen! Hier sind die ersten 5 Zeilen:")
        # zeigt die ersten Zeilen der Tabelle im Terminal an
        print(df.head()) 
        
        # 3. Jetzt kannst du die Watt-Spalte auswählen
        # ERSETZE 'watt' durch den echten Spaltennamen aus deiner Datei!
        watt_daten = df['powerOriginal']
        
        # HIER kommt später der Aufruf deiner Funktion aus analyse.py hin...
        
    except FileNotFoundError:
        print(f"Fehler: Die Datei '{dateiname}' wurde nicht gefunden.")
        print("Stelle sicher, dass sie wirklich im selben Ordner wie main.py liegt.")

if __name__ == "__main__":
    main()