from importlib.resources import files
import os

def load_data(file):
    data_dir = files('faced.data')
    files_list = os.listdir(data_dir)
    data_file = data_dir.joinpath(file)
    print(f'Files found in this directory are {files_list}')
    return data_file


