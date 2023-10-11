#! /user/bin/python3

import os
import sys

#create an archive
def create_archive(files):
    for file in files:
        try:
            file_descriptor = os.open(file, 'r')
            stat = os.fstat(file_descriptor)
            meta_data = encode_metadata(stat)
            sys.stdout.write(meta_data)

            while stat > 0:
                chunk = os.read(file_descriptor, chunk.size)
                if not chunk:
                    break
                sys.stdout.write(chunk)
            
            os.close(file_descriptor)

        except Exception as e:
            #Handle whatever exception errors arise (change as exceptions are found)
            sys.stderr.write(f"Error while processing {file}: {str(e)}")

#extract an archive
def extract_archive():
    while True:
        try:
            meta_data = sys.stdin.read(meta_data.size)
            if not meta_data:
                break
                
            stat = decode_metadata(meta_data)

            file_to_read = os.open(stat.filename, os.O_CREAT | os.O_WRONLY | os.O_TRUNC)

            while stat.size > 0:
                chunk_size = min(stat.size, chunk_size)
                chunk = sys.stdin.read(chunk_size)
                os.write(file_to_read, chunk)
                stat.size -= len(chunk)

            os.close(file_to_read)

        except Exception as e:
            sys.stderr.write(f"Error while processing {file_to_read}: {str(e)}")

#encode the metadata
def encode_metadata(static_data):
    pass

#decode the metadata
def decode_metadata(meta_data):
    pass

def main():
    #check argument length
    if len(sys.argv) < 3:
        print("Format: mytar <command> <filename> <operand> <filename")
        exit(0)