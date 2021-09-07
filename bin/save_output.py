#!/usr/bin/env python3
# save_output.py: save data on std to appropriate output file
# usage: save_output.py directory < data
# 20210608 erikt(at)xs4all.nl

import datetime
import os
import sys

assert len(sys.argv) > 1, f"usage: {sys.argv[0]} directory"
output_directory = sys.argv.pop(-1)
assert os.path.isdir(output_directory), f"not an existing directory: {output_directory}"

out_file_name_org = ""
out_file = None
for line in sys.stdin:
    out_file_name = datetime.datetime.strftime(datetime.datetime.now(), "%Y%m%d-%H.out")
    if out_file_name != out_file_name_org:
        if out_file_name_org != "":
            out_file.close()
        out_file = open(os.path.join(output_directory, out_file_name), "a")
        out_file_name_org = out_file_name
    print(line, end="", file=out_file)
if out_file_name_org != "":
    out_file.close()

