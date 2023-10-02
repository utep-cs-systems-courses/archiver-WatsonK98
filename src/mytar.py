#! /user/bin/python3
import os
import sys

def create_archive(files):
    for file in files:
        try:
            file_to_read = os.open(file, os.O_RDONLY)
            static_data = os.fstat(file_to_read)
            meta_data = encode_metadata(static_data)

            while static_data > 0:
                chunk_size = min(static_data.size, chunk_size)
                chunk = sys.stdin.read(chunk_size)
                os.write(file_to_read, chunk)
                static_data.size -= len(chunk)
            
            os.close(file_to_read)

        except Exception as e:
            #Handle whatever exception errors arise (change as exceptions are found)
            sys.stderr.write(f"Error while processing {file}: {str(e)}")

def encode_metadata(static_data):
    pass

def decode_metadata(meta_data):
    pass