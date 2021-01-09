from project_utils import create_folder_path
from project_utils.save_date_folder import save_date_folder

import datetime
import time


last_day_it_ran = None
while True:
    now = datetime.datetime.now()
    if now.day == last_day_it_ran:
        print("Sleeping")
        time.sleep(60*60)
        print("Done sleeping")
    else:
        save_date_folder()
        last_day_it_ran = now.day

