#!/usr/bin/env python
import os
import glob
import sys


# How to use:
# python3 all-test.py checkpoints_path conf_thres
def main():
    f = glob.glob(sys.argv[1] + '/*')
    for s in f:
        print(s)
        os.system('python3 -W ignore:UserWarning test.py --model_def config/malimg.cfg --data_config config/malimg.data --weights_path ' + s + ' --conf_thres ' + sys.argv[2])


if __name__ == "__main__":
    main()
