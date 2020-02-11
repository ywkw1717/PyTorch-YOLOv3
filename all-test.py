#!/usr/bin/env python
import os
import glob
import sys
import re


# How to use:
# python3 all-test.py cfg_path data_path checkpoints_path conf_thres starting_from
def main():
    cfg_path = sys.argv[1]
    data_path = sys.argv[2]
    checkpoints_path = sys.argv[3]
    conf_thres = sys.argv[4]
    starting_from = int(sys.argv[5])

    f = glob.glob(checkpoints_path + '/*')
    f = sorted(f, key=lambda x: int(re.findall(r"\d+", os.path.basename(x))[1]))

    for i in range(starting_from):
        f.pop(0)

    for s in f:
        print(s)
        os.system('python3 -W ignore:UserWarning test.py --model_def ' + cfg_path + ' --data_config ' + data_path + ' --weights_path ' + s + ' --conf_thres ' + conf_thres)


if __name__ == "__main__":
    main()
