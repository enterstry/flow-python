import sys
import logging


def func_parse(stream):
    stream.write('OUT', sys.argv[1])


def func_load_file(stream):
    file_name = stream.read()
    with open(file_name, 'r') as f:
        stream.write('OUT', f.readlines())

def func_error(stream):
    logging.log(stream.read())
