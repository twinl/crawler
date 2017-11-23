#!/usr/bin/python3 -W all
"""
    getTweetText.py: extract tweet text from json file
    usage: getTweetText.py < file
    20171123 erikt(at)xs4all.nl
"""

import json
import re
import sys

COMMAND = sys.argv[0]

for line in sys.stdin:
    try:
        jsonLine = json.loads(line)
        if "text" in jsonLine: 
           text = re.sub("\n"," ",jsonLine["text"])
           print(text)
    except: pass
sys.exit(0)
