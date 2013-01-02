

import os
import subprocess


def main():
    print os.getcwd()
    p = subprocess.Popen('pythonw main.py -r True', False)


if __name__ == '__main__':
    main()
