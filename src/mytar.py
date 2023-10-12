#! usr/bin/env python3

import os, sys      

def create_archive(file_descriptor):
    data = sys.argv[2,-2,:]
    fd = os.open(fd, 100)


def extract_archive(file_descriptor):
    data = os.open(fd, 100)

if len(sys.argv) < 3:
    print(f"Usage: ./mytar.py <command> <pointer> <filename")
    exit(1)

command = sys.argv[1]
fd = sys.argv[-1]

if command == "c":
    create_archive(fd)
elif command == "x":
    extract_archive(fd)
