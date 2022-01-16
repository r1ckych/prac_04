
import os
import shutil


DIRECTORY = 'FilesToSort'


def main():
    os.chdir(DIRECTORY)
    files = get_filenames()
    extensions = get_extensions(files)
    create_directories(extensions)
    move_files(extensions)


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

main()