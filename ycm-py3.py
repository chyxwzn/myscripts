#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import glob
import shutil

for filename in glob.glob(r"**/*.py", recursive=True):
# for filename in glob.glob(r"test.txt", recursive=True):
    with open(filename, 'r+') as pyFile:
        with open("tmp.py", 'w') as tmp:
            line = pyFile.readline()
            if line.rstrip() != '#!/usr/bin/env python3':
                if line.rstrip() != '#!/usr/bin/env python':
                    tmp.write('#!/usr/bin/env python3\n')
                else:
                    line = '#!/usr/bin/env python3\n'
            tmp.write(line)
            for line in pyFile:
                tmp.write(line)

    shutil.move("tmp.py", filename)
