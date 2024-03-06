import requests
from typing import List, Dict
import pandas as pd
from datetime import date


class CarImport:

    # constructor
    def __init__(self, brand: str):
        self.brand = brand
        self.status = "Initialized"
        self.num_cars = 0
        self.df = pd.DataFrame()


    # method to import the cars
    def get_data_from_rdw(self, auto_continue=False) -> List[Dict]:
        """
        Function to import cars from the RDW

        * brand: Brand to import
        
        Returns:
        * List of cars for the specified brand
        
        """
        # get the brand value
        brand = self.brand

        # uppercase the brand
        brand_upper = brand.upper()

        # define the RDW endpoint
        endpoint = f"https://opendata.rdw.nl/resource/m9d7-ebf2.json?merk={brand_upper}"

        # execute the request
        response = requests.get(endpoint)

        # check the response
        if response.status_code not in (200, 201):
            if auto_continue:
                pass
            else:
                raise requests.RequestException(f"Timeout {response.status_code}")

        # get the data from the response
        data = response.json()

        # check if the list is not empty
        if len(data) == 0:
            raise ValueError(f"No cars found for brand: {brand}")

        # show the number of cars imported
        num_cars = len(data)
        print(f"✅ Found {num_cars} cars for brand {brand}")

        # save the data to the object
        self.data = data

        # change the status
        self.status = "downloaded"

        # add number of cars
        self.num_cars = num_cars

    
    # convert to a DataFrame
    def convert_list_to_df(self, *args, **kwargs) -> pd.DataFrame:
        """
        Function to convert a list to a Pandas DataFrame.

        input:
        * items_list: list to convert

        returns:
        * pandas DataFrame
        """

        # get the list of cars
        items_list = self.data

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

        # add the DataFrame to self
        self.df = df_filtered

        # change the status
        self.status = "converted"

    
    # additional data cleaning
    def clean_df(self, *args, **kwargs) -> pd.DataFrame:
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

        # get the DataFrame
        df = self.df

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
        
        # return the cleaned data
        self.df = df

        # change the status
        self.status = "cleaned"


    # method for exporting the data
    def export_to_csv(self) -> None:
        """
        Function to export a DataFrame to csv

        Params:

        * df: DataFrame to export

        Returns:
        * Nothing in Python, only exported file.
        """
        # get the DataFrame
        df = self.df

        # get the name of the brand for the filename
        filename = self.brand

        # define the path to export the data frame
        file_path = f"data/{filename}.csv"

        # export with pandas
        df.to_csv(file_path, index=False)

       #print(f"✅ Saved file to {file_path}")

        # change the status
        self.status = "exported"


    # how to represent the object
    def __repr__(self) -> str:
        return f"Car import for: {self.brand} - status: {self.status} - {self.num_cars} - {self.df.head()}"