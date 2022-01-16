
import os
import shutil


DIRECTORY = 'FilesToSort'


def main():
    os.chdir(DIRECTORY)
    files = get_filenames()
    extensions = get_extensions(files)
    create_directories(extensions)
    move_files(extensions)

main()