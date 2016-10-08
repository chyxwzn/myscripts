#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import glob
import subprocess as sp
import re
import sys
import os

stream = re.compile(r'    Stream #0:(\d)')
ukr = re.compile(r'    Stream #0:(\d)\(ukr\): Audio')
fail = []
for eps in glob.glob(r'*/*.mkv', recursive=True):
    print(eps)
    err = sp.Popen(['ffmpeg', '-i', eps], stderr=sp.PIPE, universal_newlines=True).communicate()[1]
    keepSt = []
    for line in err.split('\n'):
        match = stream.match(line)
        if match:
            if not ukr.match(line):
                keepSt.append(match.group(1))
    mapSt = ['-map 0:' + st for st in keepSt]
    extrCmd = 'ffmpeg -i "' + eps + '" ' + ' '.join(mapSt) + r' -vcodec copy -acodec copy -scodec copy "' + eps.replace(r'.mkv', '') + '.extr.mkv"'
    print(extrCmd)
    ret = os.system(extrCmd)
    if ret == 0:
        os.system('rm "' + eps + '"')
        os.system('mv "' + eps.replace(r'.mkv', '') + '.extr.mkv" "' + eps + '"')
    else:
        fail.append(eps)

print("fail:")
print(fail)
