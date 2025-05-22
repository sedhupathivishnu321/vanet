import csv
from lstm_model import evaluate_lstm
from xgboost_model import evaluate_xgboost
from gnn_model import evaluate_gnn
from rl_agent import evaluate_rl

import os
os.makedirs("results/images", exist_ok=True)

# Evaluate each model
eff_lstm = evaluate_lstm()
eff_xgb = evaluate_xgboost()
eff_gnn = evaluate_gnn()
eff_rl = evaluate_rl()

# Store results in CSV
efficiency_data = [
    ['Model', 'MAE', 'RMSE', 'R2_Score', 'Avg_Travel_Time_s'],
    ['LSTM', *eff_lstm],
    ['XGBoost', *eff_xgb],
    ['GNN', *eff_gnn],
    ['Reinforcement Learning', *eff_rl]
]

with open('results/model_efficiency.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(efficiency_data)

print("All model efficiencies saved to model_efficiency.csv")
