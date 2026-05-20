import pandas as pd
from pathlib import Path


def main():
    input_path = Path("data/raw/events.csv")
    output_path = Path("data/clean/events.csv")

    df = pd.read_csv(input_path)

    # Drop rows with any missing values in required columns
    required_cols = ["user_id", "timestamp", "event_type", "duration_seconds"]

    df = df.dropna(subset=required_cols)

    # ensure event_type is valid string
    df["event_type"] = df["event_type"].astype(str)

    # remove empty/invalid placeholders
    df = df[df["event_type"].notna()]
    df = df[df["event_type"] != ""]

    # Ensure duration is numeric and positive
    df["duration_seconds"] = pd.to_numeric(df["duration_seconds"], errors="coerce")
    df = df.dropna(subset=["duration_seconds"])
    df = df[df["duration_seconds"] > 0]

    # enforce integer + positive
    df["duration_seconds"] = df["duration_seconds"].astype(int)
    df = df[df["duration_seconds"] > 0]

    # Parse timestamps (handles mixed formats)
    df["timestamp"] = pd.to_datetime(df["timestamp"], errors="coerce")
    df = df.dropna(subset=["timestamp"])

    # Normalize to ISO 8601
    df["timestamp"] = df["timestamp"].dt.strftime("%Y-%m-%dT%H:%M:%S")

    output_path.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(output_path, index=False)


if __name__ == "__main__":
    main()