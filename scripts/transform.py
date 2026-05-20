import pandas as pd
from pathlib import Path


def main():
    input_path = Path("data/clean/events.csv")
    output_path = Path("data/transformed/events.csv")

    df = pd.read_csv(input_path)

    df["date"] = pd.to_datetime(df["timestamp"]).dt.strftime("%Y-%m-%d")

    output_path.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(output_path, index=False)


if __name__ == "__main__":
    main()