#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
import glob
import os

if len(sys.argv) == 3:
    dir1 = sys.argv[1]
    dir2 = sys.argv[2]
    for item in glob.glob(dir1 + r"/*.wav", recursive=True):
        checkfile = item.replace(dir1, dir2)
        if os.path.exists(checkfile):
            print(checkfile + " is duplicated file")
            os.remove(checkfile)

