
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


main()