from pathlib import Path
import os

def create_folder_from_path():
    path = str(Path.cwd()) + '\\save date'

    try:
        os.makedirs(path)
        #path.mkdir(parents=True, exist_ok=False)
    except FileExistsError:
        print("Folder is already there")
    else:
        print("Folder was created")
    return path
