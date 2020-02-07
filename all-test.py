#!/usr/bin/env python
import os
import glob
import sys
import re


# How to use:
# python3 all-test.py data_path checkpoints_path conf_thres
def main():
    data_path = sys.argv[1]
    checkpoints_path = sys.argv[2]
    conf_thres = sys.argv[3]

    f = glob.glob(checkpoints_path + '/*')
    f = sorted(f, key=lambda x: int(re.findall(r"\d+", os.path.basename(x))[1]))

    for s in f:
        print(s)
        os.system('python3 -W ignore:UserWarning test.py --model_def config/malimg.cfg --data_config ' + data_path + ' --weights_path ' + s + ' --conf_thres ' + conf_thres)


if __name__ == "__main__":
    main()
