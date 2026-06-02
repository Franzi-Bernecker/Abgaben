from read_data import lade_aktivitaets_daten
from power_curve import power_curve 

df = lade_aktivitaets_daten("data/activity.csv")

power_data = df['PowerOriginal']  # Ersetze 'PowerOriginal' durch den tatsächlichen Spaltennamen in deiner CSV-Datei
duration = df['Duration']  # Ersetze 'Duration' durch den tatsächlichen Spaltennamen in deiner CSV-Datei

result = power_curve(power_data, duration)


