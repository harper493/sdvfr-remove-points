#!/usr/bin/python3

import re
import os
import sys

def removePoints(text):
    rx = r'(.*?)(<Folder>.*?<name>Points</name>.*?</Folder>)(.*)'
    m = re.match(rx, text, re.DOTALL)
    if m:
        return m.group(1) + m.group(3)
    return text

with open(sys.argv[1]) as infile:
    trimmed = removePoints(infile.read())
with open(sys.argv[1], 'w') as outfile:
    outfile.write(trimmed)

