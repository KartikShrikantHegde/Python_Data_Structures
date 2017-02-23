''' listdir return a list or array of all files in the directory of the argumet passed '''

import sys
import os


def List(dir):
    filenames = os.listdir(dir)
    print filenames


def main():
    List(sys.argv[1])


if __name__ == main():
    main()
