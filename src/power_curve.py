import os
import pandas as pd
import plotly.express as px


#1-2-5-Reihe als Basis für typische Power-Curve-Fenster (in Sekunden)
_STANDARD_STEPS = [
    1, 2, 5, 10, 20, 30, 60, 120, 180, 300,
    600, 900, 1200, 1800, 2700, 3600, 5400, 7200, 10800,
]


#Dynamisch Fenster auswählen
def generate_windows(total_time):
    windows = [w for w in _STANDARD_STEPS if w < total_time]
    if not windows or windows[-1] != int(total_time):
        windows.append(int(total_time))
    return windows


#Formatiert Sekunden als lesbares Label (z.B. '5s', '2min', '1h 30min').
def format_duration(seconds):
    if seconds < 60:
        return f"{seconds}s"
    minutes = seconds // 60
    rest_s = seconds % 60
    if minutes < 60:
        return f"{minutes}min" if rest_s == 0 else f"{minutes}min {rest_s}s"
    hours = minutes // 60
    rest_m = minutes % 60
    if rest_m == 0:
        return f"{hours}h"
    return f"{hours}h {rest_m}min"


#Berechnung der Power Curve
def calculate_power_curve(power_data, duration_data):
    power_values = power_data.values
    duration_values = duration_data.values
    cum_time = duration_data.cumsum().values
    total_time = cum_time[-1]

    windows = generate_windows(total_time)
    ergebnis = []

    for target_seconds in windows:
        max_power = 0

        for i in range(len(power_values)):
            start_time = cum_time[i] - duration_values[i]
            end_time = start_time + target_seconds

            total_power = 0
            total_duration = 0

            for j in range(i, len(power_values)):
                sample_start = cum_time[j] - duration_values[j]
                if sample_start >= end_time:
                    break
                total_power += power_values[j] * duration_values[j]
                total_duration += duration_values[j]

            if total_duration > 0:
                avg_power = total_power / total_duration
                if avg_power > max_power:
                    max_power = avg_power

        ergebnis.append({"Zeit": target_seconds, "Leistung": round(max_power, 1)})

    return pd.DataFrame(ergebnis)


#Plotten der Grafik
def plot_power_curve(df_result):
    fig = px.line(
        df_result, x="Zeit", y="Leistung",
        markers=True,
        title="Power Curve",
        labels={"Zeit": "Dauer", "Leistung": "Leistung (Watt)"},
        template="plotly_dark",
    )
    fig.update_traces(
        line=dict(color="#00d4ff", width=3),
        marker=dict(size=8),
        fill="tozeroy",
        fillcolor="rgba(0, 212, 255, 0.1)",
    )

    tickvals = df_result["Zeit"].tolist()
    ticktext = [format_duration(v) for v in tickvals]
    fig.update_xaxes(type="log", tickvals=tickvals, ticktext=ticktext)

    return fig


#Speichern der Grafik
def save_power_curve(fig, output_dir=None):
    if output_dir is None:
        output_dir = os.path.join(os.path.dirname(__file__), "..", "results")
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, "power_curve.png")
    fig.write_image(output_path, scale=2)
    print(f"Plot gespeichert unter: {output_path}")
    return output_path
