import argparse
import pandas as pd
import matplotlib.pyplot as plt

ALEF_BEIT = "אבגדהוזחטיכךלמםנןסעפףצץקרשת"


def process_text(text: str) -> pd.DataFrame:
    text_filtered = [c for c in text if c in ALEF_BEIT]
    df = pd.Series(text_filtered)
    count = (
        df.value_counts(normalize=True)
        .reset_index()
        .rename(columns={"index": "Value", 0: "Count"})
    )

    return count


def merge_two_counts(
    count1: pd.DataFrame,
    count2: pd.DataFrame,
    count1_name: str,
    count2_name: str,
) -> pd.DataFrame:
    merged = pd.merge(count1, count2, on="Value")
    merged.columns = ["letter", count1_name, count2_name]
    merged = merged.set_index("letter")

    return merged


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Process text file for character frequency analysis"
    )
    parser.add_argument("text_file", help="Path to the text file to analyze")
    parser.add_argument(
        "--plot",
        action="store_true",
        help="Plot the results instead of printing",
    )

    args = parser.parse_args()
    try:
        with open(args.text_file, "r", encoding="utf-8") as file:
            text = file.read()
            result = process_text(text)
            if args.plot:
                result.plot.bar()
                plt.show()
            else:
                print(result.head())
    except FileNotFoundError:
        print(f"Error: File '{args.text_file}' not found")
    except Exception as e:
        print(f"Error processing file: {str(e)}")

    process_text(result)
