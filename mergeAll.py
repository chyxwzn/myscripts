#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import glob
import os.path
import subprocess as sp

for videoFile in glob.iglob('*-video.*'):
    base = videoFile.split("-video")[0]
    audioGlob = glob.glob(base + r"-audio.*")
    if len(audioGlob) > 0:
        audioFile = audioGlob[0]
    else:
        continue
    srtGlob = glob.glob(base + ".srt")
    if len(srtGlob) > 0:
        srtFile = srtGlob[0]
    else:
        srtFile = ''
    finalFile = base + ".mkv"
    if srtFile != '':
        sp.run(['ffmpeg', '-i', videoFile, '-i', audioFile, '-i', srtFile, '-map', '0:0', '-map', '1:0', '-map', '2:0', 
            '-vcodec', 'copy', '-acodec', 'copy', '-scodec', 'copy', finalFile], stdout=sp.PIPE, stderr=sp.PIPE)
    else:
        sp.run(['ffmpeg', '-i', videoFile, '-i', audioFile, '-map', '0:0', '-map', '1:0', '-vcodec', 'copy', '-acodec', 'copy', finalFile],
                stdout=sp.PIPE, stderr=sp.PIPE)
    print("success!!! final file: " + finalFile)
    os.remove(videoFile)
    os.remove(audioFile)
    if os.path.exists(srtFile):
        os.remove(srtFile)
