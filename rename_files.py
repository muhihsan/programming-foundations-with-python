import os

def rename_files():
    #(1) get file names from a folder
    file_path = r"/home/mihsan/Projects/Udacity/Programming Foundations with Python"
    file_list = os.listdir(file_path)
    print (file_list)
    os.chdir(file_path)

    #(2) for each file, rename filename
    for file_name in file_list:
        table = str.maketrans(dict.fromkeys('0123456789'))
        new_file_name = file_name.translate(table)
        print("Old Name - " + file_name)
        print("New Name - " + new_file_name)
        os.rename(file_name, new_file_name)
rename_files()
