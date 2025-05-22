import os
import csv
from datetime import datetime
import matplotlib.pyplot as plt

# Create folders
os.makedirs('vanet_simulation_results/images/vehicle_icons', exist_ok=True)
os.makedirs('vanet_simulation_results/outputs', exist_ok=True)

# Simulation Summary
simulation_summary = {
    'start_time': "08:00 AM",
    'end_time': "08:11 AM",
    'route': "Hosur Road -> Vemana Rd -> Inner Ring Rd -> Domlur -> 100 Ft Rd",
    'total_distance_km': 9.8,
    'total_time_min': 11,
    'vehicles': 150,
    'emergency_vehicles': 5,
    'average_speed_kmph': 50,
    'congestion_level': 'Medium'
}

# Save summary to .txt
with open('vanet_simulation_results/outputs/simulation_summary.txt', 'w') as f:
    for key, val in simulation_summary.items():
        f.write(f"{key}: {val}\n")

# Create CSV for traffic efficiency
efficiency_data = [
    ['Vehicle_Type', 'Count', 'Avg_Speed_kmph', 'Wait_Time_sec'],
    ['Car', 100, 52, 18],
    ['Bus', 30, 45, 35],
    ['Ambulance', 5, 60, 2],
    ['Bike', 15, 55, 10]
]

with open('vanet_simulation_results/outputs/traffic_efficiency.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(efficiency_data)

# Plot a simple bar chart (vehicle vs speed)
vehicle_types = [row[0] for row in efficiency_data[1:]]
avg_speeds = [row[2] for row in efficiency_data[1:]]

plt.figure(figsize=(8,5))
plt.bar(vehicle_types, avg_speeds, color='skyblue')
plt.title('Average Speed by Vehicle Type')
plt.ylabel('Speed (kmph)')
plt.xlabel('Vehicle Type')
plt.savefig('vanet_simulation_results/images/route_map.png')
plt.close()

print("✅ Simulation data and visuals saved.")
