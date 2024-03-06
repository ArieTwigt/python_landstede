import os


# check if the data folder already exists
folder_name = 'data'

if not os.path.exists(folder_name):
    os.mkdir(folder_name)
    print(f"📂 Created {folder_name} folder")