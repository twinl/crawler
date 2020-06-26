#!/usr/bin/python3 -W all
"""
# merge.py: merge json output of different tweet crawlers
# usage: merge.py dir1/file1.gz [dir2/file2.gz ...]
# note: directory names (required) are used for determining the crawler names
# 20171123 erikt(at)xs4all.nl
"""

import gzip
import json
import sys

COMMAND = sys.argv.pop(0)
SOURCECOLUMNNAME = "twinl_source"

files = sys.argv
sources = {}

def getSourceName(inFile):
    pathList = inFile.split("/")
    if len(pathList) < 2 or pathList[-2] == "": return("UNKNOWN")
    else: return(pathList[-2])

def readData():
    data = {}
    for inFileName in files:
        try:
            with gzip.open(inFileName,"rb") as inFile:
                sourceName = getSourceName(inFileName)
                for row in inFile:
                    try:
                        row = row.decode("utf8")
                        jsonLine = json.loads(str(row))
                        if "id_str" in jsonLine:
                            idInt = int(jsonLine["id_str"])
                            if idInt in sources.keys(): 
                                sources[idInt].append(sourceName)
                            else:
                                sources[idInt] = [sourceName]
                                data[idInt] = jsonLine
                    except: pass
        except: sys.exit(COMMAND+": problem processing file "+inFileName)
    return(data)

def printData(data):
    for idInt in sorted(data.keys()):
        data[idInt][SOURCECOLUMNNAME] = sorted(list(set(sources[idInt])))
        print(json.dumps(data[idInt]))

def main(argv):
    data = readData()
    printData(data)
    sys.exit(0)

if __name__ == "__main__":
    sys.exit(main(sys.argv))
