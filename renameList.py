#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import glob
import shutil

with open("list.txt", "r") as fp:
    trackList = fp.readlines()
    i = 0
    for wav in glob.glob(r"*.wav", recursive=False):
        print(trackList[i][:-1])
        shutil.move(wav, trackList[i][:-1]+".wav")
        i += 1
