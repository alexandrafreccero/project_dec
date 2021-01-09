

def save_date_folder():
    # Importerar lokalt, för att unvika circular imports
    from project_utils import get_date
    from project_utils import create_folder_from_path
    from project_utils import WikipediaHandler
    
    today = get_date()
    summary = WikipediaHandler().get_summary(today)
    path = create_folder_from_path()+"\\today.txt"

    print("Storing the wikiedia summary to", path, "\nThe contents will be the following:\n\n")
    with open(path,"w+") as the_file:
        data = f"{today}\n\n{summary}"
        the_file.write(data)
        print(data)

