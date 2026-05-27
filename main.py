# 1. Pandas-Bibliothek laden
import pandas as pd
import streamlit as st

# 2. Die CSV-Datei einlesen und als DataFrame mit dem Namen 'df' speichern
df = pd.read_csv('activity.csv')

# 3. Den Inhalt des DataFrames anzeigen lassen
df.head()
st.write(df)

mean = df['PowerOriginal'].mean()
st.write(mean)

max = df['PowerOriginal'].max()
st.write(max)

import plotly.graph_objects as go
from plotly.subplots import make_subplots

# 1. Erstelle ein Layout mit einer sekundären Y-Achse
fig = make_subplots(specs=[[{"secondary_y": True}]])

# 2. Füge die Linie für die Leistung hinzu (linke Y-Achse)
fig.add_trace(
    go.Scatter(
        x=df.index,
        y=df['PowerOriginal'],
        name="Leistung (Watt)",
        mode='lines'
    ),
    secondary_y=False, # False = linke Achse
)

# 3. Füge die Linie für die Herzfrequenz hinzu (rechte Y-Achse)
fig.add_trace(
    go.Scatter(
        x=df.index,
        y=df['HeartRate'],
        name="Herzfrequenz (BPM)",
        mode='lines'
    ),
    secondary_y=True, # True = rechte Achse
)

# 4. Achsenbeschriftungen hinzufügen
fig.update_layout(title_text="Leistung und Herzfrequenz über die Zeit")
fig.update_xaxes(title_text="Zeit")
fig.update_yaxes(title_text="<b>Leistung</b> (Watt)", secondary_y=False)
fig.update_yaxes(title_text="<b>Herzfrequenz</b> (BPM)", secondary_y=True)

# 5. In Streamlit anzeigen lassen
st.plotly_chart(fig, use_container_width=True)
