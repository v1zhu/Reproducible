import pandas as pd
from pathlib import Path


def main():
    input_path = Path("data/transformed/events.csv")
    output_path = Path("data/features/events.csv")

    df = pd.read_csv(input_path)

    df["duration_minutes"] = df["duration_seconds"].astype(float) / 60.0
    df["weekday"] = pd.to_datetime(df["date"]).dt.day_name()

    output_path.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(output_path, index=False)


if __name__ == "__main__":
    main()