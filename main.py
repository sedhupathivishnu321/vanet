from data_fetch import fetch_all_data
from preprocess import preprocess_all_data
from lstm_model import run_lstm
from xgboost_model import run_xgboost
from gnn_model import run_gnn
from rl_agent import run_rl_simulation

def main():
    print("Fetching data...")
    raw_data = fetch_all_data()

    print("Preprocessing data...")
    processed_data = preprocess_all_data(raw_data)

    print("Running LSTM prediction...")
    lstm_results = run_lstm(processed_data)

    print("Running XGBoost prediction...")
    xgb_results = run_xgboost(processed_data)

    print("Running GNN congestion graph prediction...")
    gnn_results = run_gnn(processed_data)

    print("Running Reinforcement Learning signal optimization...")
    run_rl_simulation(processed_data)

    print("All models executed successfully.")

if __name__ == "__main__":
    main()
