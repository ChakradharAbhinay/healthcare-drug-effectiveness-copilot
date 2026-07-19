import pandas as pd


def load_data():
    train_path = "data/raw/drugsComTrain_raw.csv"
    test_path = "data/raw/drugsComTest_raw.csv"

    train_df = pd.read_csv(train_path)
    test_df = pd.read_csv(test_path)

    return train_df, test_df


def explore_data(train_df, test_df):
    print("=" * 50)
    print("DATASET SHAPE")
    print("=" * 50)
    print("Train shape:", train_df.shape)
    print("Test shape:", test_df.shape)

    print("\n" + "=" * 50)
    print("COLUMNS")
    print("=" * 50)
    print(train_df.columns.tolist())

    print("\n" + "=" * 50)
    print("FIRST 5 ROWS")
    print("=" * 50)
    print(train_df.head())

    print("\n" + "=" * 50)
    print("MISSING VALUES")
    print("=" * 50)
    print(train_df.isnull().sum())

    print("\n" + "=" * 50)
    print("RATING DISTRIBUTION")
    print("=" * 50)
    print(train_df["rating"].value_counts().sort_index())

    print("\n" + "=" * 50)
    print("TOP 10 DRUGS")
    print("=" * 50)
    print(train_df["drugName"].value_counts().head(10))

    print("\n" + "=" * 50)
    print("TOP 10 CONDITIONS")
    print("=" * 50)
    print(train_df["condition"].value_counts().head(10))

    print("\n" + "=" * 50)
    print("ONE SAMPLE REVIEW")
    print("=" * 50)
    sample = train_df.iloc[0]
    print("Drug:", sample["drugName"])
    print("Condition:", sample["condition"])
    print("Review:", sample["review"])
    print("Rating:", sample["rating"])


if __name__ == "__main__":
    train_df, test_df = load_data()
    explore_data(train_df, test_df)
