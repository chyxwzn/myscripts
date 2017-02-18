#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import glob
import re
import os
import shutil

# namePt = re.compile(r"(.*)-(.{11})\.(.*)")
# namePt = re.compile(r"(.*) - (.*) (\d{1,2})-(.{11})\.(mp4)")
namePt = re.compile(r"(\d{4} )(ESL.*\.m4a)")
# namePt = re.compile(r"汽车发烧音乐精选《(.*)》")
for item in glob.glob(r"*.m4a", recursive=False):
    # os.rename(item, item.replace(':', ' -'))
    match = namePt.match(item)
    if match:
        # print(match.group(2))
        # os.rename(item, match.group(2))
        try:
            shutil.move(item, match.group(2))
        except:
            print(match.group(2))
        # shutil.move(item, match.group(3)+" - "+match.group(1)+"."+match.group(5))
