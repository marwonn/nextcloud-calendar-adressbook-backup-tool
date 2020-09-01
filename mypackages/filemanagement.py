def move_files():
    import os
    import shutil
    from datetime import datetime

# creates the folder in the current working directory
    home = os.getcwd()
    today = datetime.now()
    path_dir = home + "\\backup_cal\\" + today.strftime('%Y-%m-%d')
    os.makedirs(path_dir, exist_ok=True)

# moves the downloaded files to the created folder
    files = os.listdir(home)

    for f in files:
        if f.endswith((".ics", ".vcf")):
            if os.path.isfile(os.path.join(home, f)):
                shutil.move(os.path.join(home, f), path_dir)


if __name__ == "__main__":
    move_files()
else:
    print("module 'Filemanagement' is imported")
