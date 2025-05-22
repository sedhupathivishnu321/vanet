def run_gnn(data):
    print("Running GNN on road network...")
    # Use libraries like PyTorch Geometric or DGL
    return "gnn_congestion_graph"
import math
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score

def evaluate_gnn():
    # Replace these with actual test data and model predictions
    y_true = [18, 27, 35, 45]
    y_pred = [20, 25, 34, 47]

    mae = mean_absolute_error(y_true, y_pred)
    rmse = math.sqrt(mean_squared_error(y_true, y_pred))
    r2 = r2_score(y_true, y_pred)
    avg_travel_time = sum(y_pred) / len(y_pred)

    return mae, rmse, r2, avg_travel_time

