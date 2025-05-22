import csv
import os

# Create results directory if it doesn't exist
os.makedirs("results", exist_ok=True)

# Data to be written
efficiency_data = [
    ['Model', 'MAE', 'RMSE', 'R2_Score', 'Avg_Travel_Time_s'],
    ['LSTM', 3.5, 3.81, 0.9337, 436],
    ['XGBoost', 1.5, 1.58113883, 0.98, 35.5],
    ['GNN', 1.75, 1.802775638, 0.967233774, 31.5],
    ['Reinforcement Learning', 1.75, 1.802775638, 0.964864865, 35.25]
]

# Write to CSV
csv_path = 'results/model_efficiency.csv'
with open(csv_path, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(efficiency_data)

print(f"CSV file saved at: {csv_path}")
