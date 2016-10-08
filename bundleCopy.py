import os

with open("cplist", "r") as fp:
    cplist = fp.readlines()
    for item in cplist:
        cpcmd = 'cp -rf "' + item[:-1].strip() + '" /Volumes/SHANLING/'
        print(cpcmd)
        os.system(cpcmd)
