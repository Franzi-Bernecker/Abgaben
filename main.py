
import pandas as pd
import streamlit as st
import plotly.graph_objects as go
from plotly.subplots import make_subplots


#Tabs
tabs = st.tabs(["Data", "Calculations", "Zone Summary"])


df = pd.read_csv('activity.csv')
#df.head()

with tabs[0]:
    st.write("Dataframe")
    st.write(df)

with tabs[1]: 
    
    mean = df['PowerOriginal'].mean()
    st.write("Power Mean")
    st.write(mean)

    max = df['PowerOriginal'].max()
    st.write("Power Max")
    st.write(max)

    #chart 1
    fig = make_subplots(specs=[[{"secondary_y": True}]])

    fig.add_trace(
        go.Scatter(
            x=df.index,
            y=df['PowerOriginal'],
            name="Leistung (Watt)",
            mode='lines'
        ),
        secondary_y=False,
    )

    fig.add_trace(
        go.Scatter(
            x=df.index,
            y=df['HeartRate'],
            name="Herzfrequenz (BPM)",
            mode='lines'
        ),
        secondary_y=True,
    )

    fig.update_layout(title_text="Leistung und Herzfrequenz über die Zeit")
    fig.update_xaxes(title_text="Zeit")
    fig.update_yaxes(title_text="<b>Leistung</b> (Watt)", secondary_y=False)
    fig.update_yaxes(title_text="<b>Herzfrequenz</b> (BPM)", secondary_y=True)

    st.plotly_chart(fig, use_container_width=True)


with tabs[2]:
    #Input feld
    max_hr = st.number_input("Maximale Herzfrequenz", value=220, min_value=100, max_value=220) 

    bins = [0, 0.6*max_hr, 0.7*max_hr, 0.8*max_hr, 0.9*max_hr, 1.0*max_hr]
    labels = ["Z1", "Z2", "Z3", "Z4", "Z5"]

    df['HRZone'] = pd.cut(df['HeartRate'], bins=bins, labels=labels)

    #Chart 2
    zone_colors = {
        "Z1": "blue",
        "Z2": "green",
        "Z3": "yellow",
        "Z4": "orange",
        "Z5": "red"
    }

    fig2 = make_subplots(specs=[[{"secondary_y": True}]])

    fig2.add_trace(
        go.Scatter(
            x=df.index,
            y=df['PowerOriginal'],
            name="Leistung (Watt)",
            mode='lines',
            line=dict(color='gray', width=1),
            opacity=0.5
        ),
        secondary_y=False,
    )

    for zone in labels:
        mask = df['HRZone'] == zone
        if mask.any():
            fig2.add_trace(
                go.Scatter(
                    x=df[mask].index,
                    y=df[mask]['HeartRate'],
                    name=f"HR {zone}",
                    mode='markers',
                    marker=dict(color=zone_colors[zone], size=3),
                ),
                secondary_y=True,
            )

    fig2.update_layout(title_text="Herzfrequenz (nach Zonen) und Leistung")
    fig2.update_xaxes(title_text="Zeit (Sekunden)")
    fig2.update_yaxes(title_text="<b>Leistung</b> (Watt)", secondary_y=False)
    fig2.update_yaxes(title_text="<b>Herzfrequenz</b> (BPM)", secondary_y=True)

    st.plotly_chart(fig2, use_container_width=True)

    #Zone Summary
    time_in_zone_sec = df["HRZone"].value_counts().reindex(labels, fill_value=0)
    avg_power_per_zone = df.groupby('HRZone')['PowerOriginal'].mean()

    zone_summary = pd.DataFrame({
        "Time in zone (sec)": time_in_zone_sec,
        "Average power (W)": avg_power_per_zone
    })

    st.write("Zone Summary")
    st.write(zone_summary)
