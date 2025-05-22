import pandas as pd
import random
import os

# Load data
df = pd.read_csv('vanet_simulation_results/outputs/traffic_efficiency.csv')

# Decision logic based on average wait time and speed
def analyze_traffic(df):
    alerts = []
    for index, row in df.iterrows():
        if index == 0:
            continue  # Skip header
        vehicle, count, speed, wait = row
        if vehicle == 'Ambulance' and wait > 5:
            alerts.append(f"⚠️ Delay detected for Ambulance. Wait Time: {wait}s")
        if speed < 40:
            alerts.append(f"🛑 Slow traffic for {vehicle}. Speed: {speed} km/h")
    return alerts

# Suggest signal timing changes
def optimize_signals(df):
    changes = {}
    for index, row in df.iterrows():
        if index == 0:
            continue
        vehicle, _, speed, wait = row
        if wait > 20:
            changes[vehicle] = "+5s green light"
        else:
            changes[vehicle] = "No change"
    return changes

# Run Analysis
alerts = analyze_traffic(df.values.tolist())
adjustments = optimize_signals(df.values.tolist())

# Print outcomes
print("🔍 Traffic Efficiency Analysis:")
for alert in alerts:
    print(alert)

print("\n🚦 Suggested Signal Adjustments:")
for k, v in adjustments.items():
    print(f"{k}: {v}")

# Save all outputs in a CSV log
with open('vanet_simulation_results/outputs/traffic_management_log.csv', 'w', newline='') as log:
    writer = csv.writer(log)
    writer.writerow(['Vehicle_Type', 'Adjustment'])
    for k, v in adjustments.items():
        writer.writerow([k, v])

print("\n✅ Traffic management decisions logged.")
