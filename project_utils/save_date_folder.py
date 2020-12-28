from project_utils import get_date
from project_utils import create_folder_from_path

def save_date_folder():
    f=open(create_folder_from_path()+"\\today.txt","w+")
    f.write (str(get_date()))
    print(f.read())

