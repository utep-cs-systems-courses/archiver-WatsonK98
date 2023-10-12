#! usr/bin/env python3

import os, sys      

if len(sys.argv) < 3:
    print("Appropriate command is mytar <command> <filename> <command line arg> <filename>")
    exit()
command = sys.argv[1]

if command == 'c':
    for arg in sys.argv:
        if arg != 'c' and arg != './mytar.py':
            data = b''
            inputFile = os.open(arg, os.O_RDONLY)
            read = os.read(inputFile, 100)
            while read != b'':
                data = data+read
                read = os.read(inputFile, 100)
            byte = str(len(arg))+':'+arg+str(len(data))+':'
            byte = byte.encode()
            byte = byte + data
            os.write(1, byte)
            os.close(inputFile)

if command == 'x':
    inputFile = os.open(sys.argv[2], os.O_RDONLY)
    data = ''
    read = os.read(inputFile, 100).decode()
    while read != '':
        data = data+read
        read = os.read(inputFile, 100).decode()
    lines = data.split('\n')
