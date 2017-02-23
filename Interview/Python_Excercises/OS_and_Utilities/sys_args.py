import sys
import os


def List(dir):
    filenames = os.listdir(dir)
    for filename in filenames:
        path = os.path.join(dir,filename)
        print path
        print os.path.abspath(path)

def main():
    List(sys.argv[1])


if __name__ == main():
    main()