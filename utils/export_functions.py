import pandas as pd

def export_to_csv(df: pd.DataFrame, filename="export") -> None:
    """
    Function to export a DataFrame to csv

    Params:

    * df: DataFrame to export

    Returns:
    * Nothing in Python, only exported file.
    """

    # define the path to export the data frame
    file_path = f"data/{filename}.csv"

    # export with pandas
    df.to_csv(file_path, index=False)

    print(f"✅ Saved file to {file_path}")