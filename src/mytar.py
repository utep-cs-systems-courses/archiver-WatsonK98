#!/usr/bin/env python3

import os
import sys

def create_archive(output_file, data):
    for entry in data:
        name = entry[0]
        content = entry[1]
        byte = f"{name}\n{content}\n".encode()
        output_file.write(byte)

def extract_archive(input_file):
    data = input_file.read().decode()
    lines = data.strip().split('\n')
    
    for i in range(0, len(lines), 2):
        name = lines[i]
        content = lines[i + 1]
        print(f"Extracting file: {name}")
        print(f"File content: {content}")

if len(sys.argv) < 3:
    print("Appropriate command is mytar <command> <filename> <command line arg> <filename>")
    exit()

command = sys.argv[1]

if command == 'c':
    if len(sys.argv) < 4:
        print("Usage: mytar c <string1> <string2> ... > output.txt")
    else:
        data = [(arg, arg.encode()) for arg in sys.argv[2:]]
        create_archive(sys.stdout, data)
elif command == 'x':
    extract_archive(sys.stdin)
else:
    print("Invalid command: Use 'c' for create or 'x' for extract.")
