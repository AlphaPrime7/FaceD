from __future__ import absolute_import

import os
from pathlib import Path
from typing import Optional

def make_init(initdir: Optional[str] = None):
    pwd = Path(os.getcwd())
    pwd = pwd.as_posix()
    file_dir = pwd + '/' + initdir

    INIT_FILE = '__init__.py'

    try:
        if initdir is None:
            f = open(INIT_FILE, 'x')
        else:
            INIT_FILE = file_dir + '/' + INIT_FILE
            f = open(INIT_FILE, 'x')
        return f
    except (FileExistsError):
        if os.path.exists(INIT_FILE):
            print(f'{INIT_FILE} already exists. Delete it and try again!')
    except (FileNotFoundError):
        if not os.path.exists(file_dir):
            print(f'{file_dir} does NOT exist. Create the directory and try again!')



