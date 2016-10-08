import codecs
import glob
import os

for cue in glob.glob(r"**/CDImage.cue", recursive=True):
    with codecs.open(cue, "r", "cp936") as cuefp:
        try:
            contents = cuefp.readlines()
            with codecs.open(cue+".bak", "w", "utf-8") as tmpfp:
                tmpfp.writelines(contents)
                tmpfp.close()
        except:
            cuefp.close()
            print(cue + ": not cp936 encoding")
            continue
        cuefp.close()
        os.replace(cue+".bak", cue)


