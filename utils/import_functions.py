import requests
from typing import List, Dict

def get_data_from_rdw(brand: str) -> List[Dict]:
    """
    Function to import cars from the RDW

    * brand: Brand to import
    
    Returns:
    * List of cars for the specified brand
    
    """
    # uppercase the brand
    brand_upper = brand.upper()

    # define the RDW endpoint
    endpoint = f"https://opendata.rdw.nl/resource/m9d7-ebf2.json?merk={brand_upper}"

    # execute the request
    response = requests.get(endpoint)

    # check the response
    if response.status_code not in (200, 201):
        raise requests.RequestException(f"Timeout {response.status_code}")

    # get the data from the response
    data = response.json()

    # check if the list is not empty
    if len(data) == 0:
        raise ValueError(f"No cars found for brand: {brand}")

    # show the number of cars imported
    num_cars = len(data)
    print(f"✅ Found {num_cars} cars for brand {brand}")

    return data