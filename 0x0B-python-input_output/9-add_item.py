#!/usr/bin/python3
import json
import os.path
import sys

save_to_json_file = __import__('7-save_to_json_file').save_to_json_file
load_from_json_file = __import__('8-load_from_json_file').load_from_json_file

file = "add_item.json"
if os.path.isfile(file):
    ob = load_from_json_file(file)
else:
    ob = []
ob.extend(sys.argv[1:])
save_to_json_file(ob, file)
