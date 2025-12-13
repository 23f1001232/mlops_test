import pandas as pd
import os

def split_transactions(input_path, output_dir):
    df = pd.read_csv(input_path)

    df = df.sort_values("Time").reset_index(drop=True)

    midpoint = len(df) // 2
    df_2022 = df.iloc[:midpoint]
    df_2023 = df.iloc[midpoint:]

    os.makedirs(output_dir, exist_ok=True)

    df_2022.to_csv(f"{output_dir}/transactions_2022.csv", index=False)
    df_2023.to_csv(f"{output_dir}/transactions_2023.csv", index=False)

    print("Saved v0 and v1 datasets")

if __name__ == "__main__":
    split_transactions(
        "orig_data/transactions.csv",
        "data_orig"
    )

