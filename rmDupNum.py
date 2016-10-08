#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import glob
import re
import shutil

namePt = re.compile(r"(\d{1,2}\.)(.*\.wav)")
for wav in glob.glob(r"**/*.wav", recursive=True):
    match = namePt.match(wav)
    if match:
        # print(match.group(2))
        shutil.move(wav, match.group(2))
