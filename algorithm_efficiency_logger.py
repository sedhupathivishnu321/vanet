import csv
import os
import matplotlib.pyplot as plt

# Create output folder
os.makedirs('vanet_simulation_results/outputs', exist_ok=True)

# Define efficiency data
efficiency_data = [
    ['Algorithm', 'Avg_Travel_Time_s', 'Packet_Delivery_Ratio_%', 'Avg_Speed_kmph', 'Emergency_Clearance_s'],
    ['Dijkstra', 520, 89.5, 45, 18],
    ['AODV', 495, 91.2, 48, 15],
    ['Genetic Algorithm', 470, 94.0, 52, 12],
    ['Reinforcement Learning', 440, 96.5, 56, 8],
    ['Fuzzy Logic Controller', 460, 93.1, 50, 10],
]

# Save to CSV
output_path = 'vanet_simulation_results/outputs/algorithm_efficiency.csv'
with open(output_path, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(efficiency_data)

print("✅ Efficiency results for algorithms saved.")

# Plotting performance (example: Avg Travel Time)
algos = [row[0] for row in efficiency_data[1:]]
times = [row[1] for row in efficiency_data[1:]]

plt.figure(figsize=(8,5))
plt.bar(algos, times, color='orange')
plt.title('Average Travel Time per Algorithm')
plt.ylabel('Travel Time (s)')
plt.xticks(rotation=20)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.savefig('vanet_simulation_results/images/algorithm_travel_time.png')
plt.close()

print("📈 Graph saved: algorithm_travel_time.png")
