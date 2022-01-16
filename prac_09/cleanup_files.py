"""
CP1404/CP5632 Practical
Demos of various os module examples
"""
import os


def main():
    """Demo os module functions."""
    print("Starting directory is: {}".format(os.getcwd()))

    # Change to desired directory
    os.chdir('Lyrics/')

    dir_list = os.listdir('.')

    rename_files(dir_list)


def rename_files(dir_list):
    for dir in dir_list:
        os.chdir(str(dir))
        for filename in os.listdir('.'):
            if not os.path.isdir(filename):
                new_name = get_fixed_filename(filename)
                os.rename(filename, new_name)
        os.chdir('..')


def get_fixed_filename(filename):
    """Return a 'fixed' version of filename."""
    new_name = filename.replace(" ", "_").replace(".TXT", ".txt")
    new_name_chars = list(filename)

    for i, char in enumerate(new_name_chars):
        if i > 0 and char.isupper() and new_name_chars[i - 1].isalpha():
            new_name_chars.insert(i, "_")
        filename = "".join(new_name_chars)

    filename = filename.title().replace(".Txt", ".txt")
    return filename


main()
