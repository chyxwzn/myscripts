#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import glob
import os.path
import subprocess as sp

for srtFile in glob.iglob('**/*.srt', recursive=True):
    if os.path.exists(os.path.splitext(srtFile)[0]+".mp4"):
        videoFile = os.path.splitext(srtFile)[0]+".mp4"
    elif os.path.exists(os.path.splitext(srtFile)[0]+".mkv"):
        videoFile = os.path.splitext(srtFile)[0]+"_tmp.mkv"
        os.rename(os.path.splitext(srtFile)[0]+".mkv", videoFile)
    else:
        continue
    finalFile = os.path.splitext(srtFile)[0]+".mkv"
    result = sp.run(['ffmpeg', '-i', videoFile, '-i', srtFile, '-map', '0:0', '-map', '0:1', '-map', '1:0', 
        '-vcodec', 'copy', '-acodec', 'copy', '-scodec', 'copy', finalFile], stdout=sp.PIPE, stderr=sp.PIPE)
    if result.returncode == 0:
        print("success!!! final file: " + finalFile)
        os.remove(videoFile)
        os.remove(srtFile)
    else:
        print("failed to merge video and subtitle file, srt: " + srtFile)
