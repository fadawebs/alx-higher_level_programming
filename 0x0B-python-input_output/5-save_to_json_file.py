#!/usr/bin/python3
'''
module
'''
import json


def save_to_json_file(my_obj, filename):
    '''
    accepts Python object and sends JSON representation to file
    '''
    with open(filename, 'w') as f:
        f.write(json.dumps(my_obj))
