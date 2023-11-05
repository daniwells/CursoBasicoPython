import os

def scan_folders(folder_start):
    files = os.listdir(folder_start)

    for file in files:
        print(file)

path = 'D:\Users\Micro\PycharmProjects'
scan_folders(path)