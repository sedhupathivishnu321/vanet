def run_rl_simulation(data):
    print("Running RL-based signal timing optimization...")
    # Q-learning or DQN logic here
    return "rl_simulation_results"
import math
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score

def evaluate_rl():
    # Replace these with actual values from RL simulation
    y_true = [22, 31, 39, 48]
    y_pred = [21, 33, 37, 50]

    mae = mean_absolute_error(y_true, y_pred)
    rmse = math.sqrt(mean_squared_error(y_true, y_pred))
    r2 = r2_score(y_true, y_pred)
    avg_travel_time = sum(y_pred) / len(y_pred)

    return mae, rmse, r2, avg_travel_time

