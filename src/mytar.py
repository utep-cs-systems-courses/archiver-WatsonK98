#! /usr/bin/env python3

import os, sys      


command = sys.argv[1]

if command == "c":
    create_archive(fd)
elif command == "x":
    extract_archive(fd)
