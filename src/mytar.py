#! /user/bin/python3

import os
import sys

def create_archive(files):
    for file in files:
        try:
            file_to_read = os.open(file, 'r')
            static_data = os.fstat(file_to_read)
            meta_data = encode_metadata(static_data)
            sys.stdout.write(meta_data)

            while static_data > 0:
                chunk = os.read(file_to_read, chunk_size)
                if not chunk:
                    break
                sys.stdout.write(chunk)
            
            os.close(file_to_read)

        except Exception as e:
            #Handle whatever exception errors arise (change as exceptions are found)
            sys.stderr.write(f"Error while processing {file}: {str(e)}")

def extract_archive():
    while True:
        try:
            meta_data = sys.stdin.read(meta_data.__sizeof__)
            if not meta_data:
                break
                
            static_data = decode_metadata(meta_data)

            file_to_read = os.open(static_data.filename, os.O_CREAT | os.O_WRONLY | os.O_TRUNC)

            while static_data.size > 0:
                chunk_size = min(static_data.size, chunk_size)
                chunk = sys.stdin.read(chunk_size)
                os.write(file_to_read, chunk)
                static_data.size -= len(chunk)

            os.close(file_to_read)

        except Exception as e:
            sys.stderr.write(f"Error while processing {file}: {str(e)}")

def encode_metadata(static_data):
    pass

def decode_metadata(meta_data):
    pass

def main(self):
    if(sys.argv.__len__<3):
        print(f"Error in formatting")
        exit(0)
    