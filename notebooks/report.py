import marimo as mo

app = mo.App()

@app.cell
def _():
    import pandas as pd
    import matplotlib.pyplot as plt

    df = pd.read_csv("data/features/events.csv")

    plt.hist(df["duration_minutes"], bins=30)
    plt.title("Distribution of Event Duration (minutes)")
    plt.xlabel("Duration (minutes)")
    plt.ylabel("Frequency")
    plt.show()

    return df


if __name__ == "__main__":
    app.run()