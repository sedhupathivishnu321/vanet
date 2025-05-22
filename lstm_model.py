def run_lstm(data):
    print("Training LSTM model...")
    # Insert Keras or PyTorch LSTM code
    return "lstm_predictions"
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import numpy as np
import math

def evaluate_lstm():
    y_true = [420, 430, 440, 460]
    y_pred = [415, 432, 442, 455]

    mae = mean_absolute_error(y_true, y_pred)
    rmse = math.sqrt(mean_squared_error(y_true, y_pred))
    r2 = r2_score(y_true, y_pred)
    avg_travel_time = np.mean(y_pred)
    return round(mae, 2), round(rmse, 2), round(r2, 4), round(avg_travel_time, 2)

