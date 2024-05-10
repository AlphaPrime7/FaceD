import os
from pathlib import Path
import tempfile
from zipfile import *
from PIL import Image
import pytesseract
import matplotlib.pyplot as plt
import importlib.resources as importlib_resources

def unzip_files(zipf:str =None, tmpdir:str=None) -> Path:

    if tmpdir is None:
        with tempfile.TemporaryDirectory(prefix='zip',delete=False) as tmpdir:
            print(f"Created a temporary directory: {tmpdir}")
            pzf_call = PyZipFile(zipf,mode='r')
            extracted_files = pzf_call.extractall(tmpdir)
            print(f"Files found in a temporary directory: {tmpdir}")     
    elif tmpdir is not None:
        if os.path.exists(tmpdir):
            directory = "zippo"
            tmpdir = os.path.join(tmpdir, directory) 
            mode = 0o666
            os.mkdir(tmpdir, mode) 
            print(f'A folder {tmpdir} was created in the present working directory')
        else:
            pwd = Path(os.getcwd())
            pwd = pwd.as_posix()
            directory = "zippo"
            tmpdir = os.path.join(pwd, directory) 
            mode = 0o666
            os.mkdir(tmpdir, mode) 
            print(f'A folder {tmpdir} was created in the present working directory')
        pzf_call = PyZipFile(zipf)
        extracted_files = pzf_call.extractall(tmpdir)
        print(f'Check this {tmpdir} for the extracted files')
    return tmpdir
    
def deletion_prompt():
    user_input = ''
    
    user_input = input('Are you sure you want to delete a non-empty directory: 1) Yes | 2) No | 3) Maybe [1/2/3]? ')

    if user_input == '1':
        print('You picked Yes')
    elif user_input == '2':
        print('You picked No')
    elif user_input == '3':
        print('You picked Maybe')

    return user_input

def delete_folder(dir:str, empty_folder:bool = False):
    import pathlib
    import shutil 

    if empty_folder:
        empty_dir = dir
        path = pathlib.Path(empty_dir)
        path.rmdir()
        print("Deleted '%s' directory successfully" % empty_dir)

    else:
        non_empty_dir = dir
        ui = deletion_prompt()
        if ui == '1':
            shutil.rmtree(non_empty_dir, ignore_errors=True)
            print("Deleted non-empty '%s' directory successfully" % dir)
            print("If you mistakenly deleted these files, check the recycle bin and restore them")
        else:
            print("Non-empty '%s' directory will NOT be deleted" % dir)

def create_image_path(unzipped_dir:str):
    from pathlib import Path
    prelim_list = os.listdir(unzipped_dir)
    unzipped_dir = Path(unzipped_dir)
    unzipped_dir = unzipped_dir.as_posix()

    img_list = []
    for i in prelim_list:
        new_path = unzipped_dir + '/' + i
        img_list.append(new_path)
    return img_list

def make_text_dict(zfile):
    text_dict = {}

    zf_class = ZipFile(zfile, mode='r')
    finfo = ZipFile(zfile, mode='r').infolist()

    for i in finfo: 
        img = Image.open(zf_class.open(i.filename)) 
        text = pytesseract.image_to_string(img)
        #text = format_words(text)
        text_dict[i.filename] = text
    return text_dict

def make_thumbnail(face, size_tuple=None):
    if size_tuple is None:
        MAX_SIZE = (200,200)
    else:
        size_tuple = size_tuple
    face = face.resize(MAX_SIZE)
    return face

def in_display(canvas):
    plt.imshow(canvas)
    plt.axis('off')
    plt.show()

def load_test():
    pkg = importlib_resources.files("faced")
    zipf = pkg / 'data' / 'test.zip'
    with importlib_resources.as_file(zipf) as path:
        return path
    
def load_lab():
    pkg = importlib_resources.files("faced")
    zipf = pkg / 'data' / 'lab.zip'
    with importlib_resources.as_file(zipf) as path:
        return path

def load_mark():
    pkg = importlib_resources.files("faced")
    zipf = pkg / 'data' / 'mark.png'
    with importlib_resources.as_file(zipf) as path:
        return path
