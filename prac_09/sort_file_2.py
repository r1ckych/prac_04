
import os
import shutil


DIRECTORY = "FilesToSort"


def main():
    os.chdir(DIRECTORY)
    files = get_filenames()
    extensions = get_extensions(files)

    if not files:
        print("No files could be found!")
    else:
        user_folders = []
        folder_sorting = {}
        for extension in extensions:
            user_folder = input(f"What category would you like to sort {extension} files into? ")
            if user_folder not in user_folders:
                user_folders.append(user_folder)
            folder_sorting[extension] = user_folder

        create_directories(user_folders)
        move_files(folder_sorting)


def get_filenames():
    filenames = []
    for filename in os.listdir('.'):
        if not os.path.isdir(filename):
            filenames.append(filename)
    return filenames


def get_extensions(files):
    extensions = []
    for file in files:
        for i, char in enumerate(file):
            if char == ".":
                new_extensions = file[i+1: len(file)]
                if new_extensions not in extensions:
                    extensions.append(new_extensions)
    return extensions


def create_directories(folders):
    for folder in folders:
        if folder not in os.listdir('.'):
            os.mkdir(folder)


def move_files(sorting_dictionary):
        for file in get_filenames():
            for i, char in enumerate(file):
                if char == '.':
                    file_extension = file[i + 1: len(file)]
                    shutil.move(file, sorting_dictionary[file_extension])


main()
