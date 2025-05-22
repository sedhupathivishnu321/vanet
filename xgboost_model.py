def run_xgboost(data):
    print("Training XGBoost model...")
    # Insert sklearn or xgboost logic
    return "xgb_predictions"
import math
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score

def evaluate_xgboost():
    # Sample prediction (replace this with your real model and test data)
    y_true = [20, 30, 40, 50]  # Ground truth values
    y_pred = [22, 32, 39, 49]  # Model predictions

    mae = mean_absolute_error(y_true, y_pred)
    rmse = math.sqrt(mean_squared_error(y_true, y_pred))
    r2 = r2_score(y_true, y_pred)
    avg_travel_time = sum(y_pred) / len(y_pred)

    return mae, rmse, r2, avg_travel_time

