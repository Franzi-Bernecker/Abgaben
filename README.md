# Abgabe 2 – Activity Dashboard

Streamlit-Anwendung zur Auswertung von Aktivitätsdaten aus `activity.csv`. Angezeigt werden Leistung, Herzfrequenz und Herzfrequenz-Zonen (Z1–Z5) auf Basis einstellbarer Schwellenwerte.

---

## Funktionen

Die Oberfläche ist in drei Tabs gegliedert:

| Tab | Inhalt |
|-----|--------|
| **Data** | Rohdaten als Dataframe |
| **Calculations** | Mittelwert und Maximum der Leistung; Diagramm Leistung und Herzfrequenz über die Zeit (zwei y-Achsen) |
| **Zone Summary** | Zoneneinteilung nach maximaler Herzfrequenz, farbcodierter Plot, Tabelle mit Verweildauer pro Zone und mittlerer Leistung |

Die Zonen entsprechen Prozentanteilen der maximalen Herzfrequenz (Standard: 220, im UI anpassbar). Visualisierung mit `pd.cut` und Plotly.

---

## Installation und Start

Voraussetzungen: **Python 3.14**, **PDM**.

```bash
pdm install
pdm run streamlit run main.py
```

Die Anwendung ist unter `http://localhost:8501` erreichbar (Port kann abweichen; URL siehe Terminal).

Empfohlen wird der Start über `pdm run`, damit die Abhängigkeiten aus der Projektumgebung verwendet werden.

---

## Projektstruktur

```
.
├── main.py              # Streamlit-App
├── activity.csv         # Eingabedaten
├── pyproject.toml       # Abhängigkeiten (PDM)
└── docs/images/         # optionale HTML-Exports der Diagramme
```

---

## Datenformat

`activity.csv` muss mindestens folgende Spalten enthalten:

- `HeartRate` – Herzfrequenz (BPM)
- `PowerOriginal` – Leistung (Watt)

Weitere Spalten werden nicht ausgewertet.

---

## Abhängigkeiten

- **Streamlit** – Web-Oberfläche
- **Pandas** – Datenverarbeitung
- **Plotly** – Diagramme (Subplots, sekundäre y-Achse)

---

## Autoren

- Franzi Bernecker
- Laurenz Keller

Software Engineering, MCI – Abgabe 2.
