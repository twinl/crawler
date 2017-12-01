#!/usr/bin/python3 -W all
"""
    splitTweetFile.py: split file with tweets in hourly files
    usage: splitTweetFile.py < file
    notes: writes output in yearmonthday-hour.out
           expected format: "created_at":"Fri Oct 06 20:00:30 +0000 2017"
    20171201 erikt(at)xs4all.nl
"""

import datetime
import json
import os
import sys

COMMAND = sys.argv[0]
DATEFIELD = "created_at"
OFFSET = datetime.timedelta(seconds=7200)

def writeFile(outFileName,jsonLine,fileData):
    if outFileName != fileData["lastFileName"]:
        if fileData["lastFile"] != None: fileData["lastFile"].close()
        if not outFileName in fileData["files"] and \
           os.path.exists(outFileName):
            sys.stderr.write(COMMAND+": file "+outFileName+" already exists!\n")
            sys.exit(1)
        fileData["lastFile"] = open(outFileName,"a")
        fileData["lastFileName"] = outFileName
        if not outFileName in fileData["files"]: 
            fileData["files"][outFileName] = True
    fileData["lastFile"].write(json.dumps(jsonLine)+"\n")
    return(fileData)

def main(argv):
    fileData = { "lastFile":None, "lastFileName":"", "files":{} }
    for line in sys.stdin:
        try: jsonLine = json.loads(line)
        except: continue
        if not DATEFIELD in jsonLine: continue
        date = datetime.datetime.strptime(jsonLine[DATEFIELD], \
                                          "%a %b %d %H:%M:%S %z %Y")
        date += OFFSET
        outFileName = date.strftime("%Y%m%d-%H.out")
        fileData = writeFile(outFileName,jsonLine,fileData)
    if fileData["lastFileName"] != "": fileData["lastFile"].close()
    return(0)

if __name__ == "__main__":
    sys.exit(main(sys.argv))
