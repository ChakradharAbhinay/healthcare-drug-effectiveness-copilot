import pandas as pd

TRAIN_PATH = "data/raw/drugsComTrain_raw.csv"
TEST_PATH = "data/raw/drugsComTest_raw.csv"


def load_data():
    train_df = pd.read_csv(TRAIN_PATH)
    test_df = pd.read_csv(TEST_PATH)
    return train_df, test_df


def add_basic_features(df):
    df = df.copy()
    df["review_length"] = df["review"].astype(str).str.len()
    df["review_word_count"] = df["review"].astype(str).str.split().str.len()
    return df


def print_section(title):
    print("\n" + "=" * 60)
    print(title)
    print("=" * 60)


def run_eda(train_df, test_df):
    train_df = add_basic_features(train_df)
    test_df = add_basic_features(test_df)

    print_section("DATASET SHAPES")
    print("Train shape:", train_df.shape)
    print("Test shape:", test_df.shape)

    print_section("COLUMN DATA TYPES")
    print(train_df.dtypes)

    print_section("MISSING VALUES - TRAIN")
    print(train_df.isnull().sum())

    print_section("MISSING VALUES PERCENTAGE - TRAIN")
    missing_percent = (train_df.isnull().sum() / len(train_df)) * 100
    print(missing_percent.sort_values(ascending=False))

    print_section("RATING DISTRIBUTION")
    print(train_df["rating"].value_counts().sort_index())

    print_section("RATING DISTRIBUTION PERCENTAGE")
    rating_percent = train_df["rating"].value_counts(normalize=True).sort_index() * 100
    print(rating_percent)

    print_section("USEFUL COUNT SUMMARY")
    print(train_df["usefulCount"].describe())

    print_section("REVIEW LENGTH SUMMARY")
    print(train_df[["review_length", "review_word_count"]].describe())

    print_section("TOP 10 DRUGS")
    print(train_df["drugName"].value_counts().head(10))

    print_section("TOP 10 CONDITIONS")
    print(train_df["condition"].value_counts().head(10))

    print_section("NUMERIC CORRELATION")
    numeric_cols = ["rating", "usefulCount", "review_length", "review_word_count"]
    print(train_df[numeric_cols].corr())

    print_section("TARGET LEAKAGE CHECK")
    print("Target column: rating")
    print("Potential input columns: drugName, condition, review, usefulCount")
    print("Columns to avoid as direct model input: uniqueID, date")
    print(
        "Note: usefulCount may be risky because it is user feedback collected after the review was posted. "
        "For the first baseline model, we can train with review text only to avoid leakage."
    )

    print_section("SAMPLE ROW")
    sample = train_df.iloc[0]
    print("Drug:", sample["drugName"])
    print("Condition:", sample["condition"])
    print("Review:", sample["review"])
    print("Rating:", sample["rating"])


if __name__ == "__main__":
    train_data, test_data = load_data()
    run_eda(train_data, test_data)
