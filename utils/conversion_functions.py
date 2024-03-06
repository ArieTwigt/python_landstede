import pandas as pd
from typing import List
from datetime import date

def convert_list_to_df(items_list: List, *args, **kwargs) -> pd.DataFrame:
    """
    Function to convert a list to a Pandas DataFrame.

    input:
    * items_list: list to convert

    returns:
    * pandas DataFrame
    """

    # convert the list to a pandas DataFrame
    df = pd.DataFrame(items_list)

    # filter for the columns if specified
    if len(args) == 0:
        df_filtered = df
    else:
        # convert the 'args' tuple to a list
        columns_list = list(args)
        df_filtered = df[columns_list]

    # rename the columns
    df_filtered.rename(columns=kwargs, inplace=True)

    return df_filtered


def clean_df(df: pd.DataFrame, *args, **kwargs) -> pd.DataFrame:
    """
    Function to clean the DataFrame
    
    Steps:
    * Modify data types
    * Deal with empty values
    * Remove extreme values (low and high)
    * Parsing the dates

    Input:
    * df: DataFrame to convert
    * *args: Columns to check for empty and extreme values
    * **kwargs: Mapping for the columns and data types to convert
    """

    # 1. convert to the right data types
    for col, dtype in kwargs.items():
        print(f"Convert {col} to data type {dtype}")
        # if the column is a date
        if dtype == date:
            df[col] = pd.to_datetime(df[col])
        else:
            # catch errors for NaN-values
            try:
                df[col] = df[col].astype(dtype)
            except ValueError:
                df[col] = df[col].fillna(0)
                df[col] = df[col].astype(dtype)


    # 2. remove rows with NaN for both 'datum_tenaamstelling' and prijs
    columns_list = list(args)
    df.dropna(subset=columns_list, inplace=True)

    # 3. filter for extreme values
    for col in columns_list:
        # filter the data frame for extreme low values
         df =df[df[col] > 0]
    
    return df