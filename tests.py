from utils.import_functions import get_data_from_rdw
from utils.conversion_functions import convert_list_to_df


selected_brand = "audi"

# get the data from RDW
cars_list = get_data_from_rdw(selected_brand)
cars_df = convert_list_to_df(cars_list, "handelsbenaming", "catalogusprijs", 
                                        handelsbenaming="model", 
                                        catalogusprijs="prijs")


# test getting data from RDW
def test_get_data_from_rdw_basic():

    # check if we have 1000 records
    assert len(cars_list) == 1000

    # check if the type is a list
    assert type(cars_list) == list


# test the values from the data
def test_get_data_from_rdw_values():

    # check if the value of "merk" is the right value
    imported_brand_first = cars_list[0]['merk']
    imported_brand_last = cars_list[-1]['merk']
    
    assert imported_brand_first == selected_brand.upper()
    assert imported_brand_last == selected_brand.upper()


# test if the structure of the DataFrame is right
def test_data_frame_structure():

    # check if we have the right column names
    assert list(cars_df.columns) == ['model', 'prijs']