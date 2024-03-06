from utils.cars import CarImport
from datetime import date
from tqdm import tqdm

# specify brands to import
brands_list = ['audi', 'bmw', 'tesla', 'toyota', 'kia', 'hyundai', 'arie', 'ford', 'porsche']

# loop trough the data
for brand in tqdm(brands_list):
    # create a car_import instance
    car_import = CarImport(brand)

    # import the cars
    try:
        car_import.get_data_from_rdw()
    except ValueError:
        print(f"Error for {brand}")
        continue

    # convert the data
    car_import.convert_list_to_df("kenteken", 
                                    "handelsbenaming", 
                                    "catalogusprijs", 
                                    "aantal_cilinders", 
                                    "datum_tenaamstelling",
                                    handelsbenaming="model", 
                                    catalogusprijs="prijs")


    # clean the data
    car_import.clean_df("prijs", "aantal_cilinders", 
                        prijs=float,
                        aantal_cilinders=int,
                        datum_tenaamstelling=date)


    # export the data
    car_import.export_to_csv()

