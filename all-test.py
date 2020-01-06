#!/usr/bin/env python
import os
import glob


def main():
    f = glob.glob('./checkpoints/*')
    for s in f:
        print(s)
        os.system('python3 -W ignore:UserWarning test.py --model_def config/malimg.cfg --data_config config/malimg.data --weights_path ' + s + ' --conf_thres 0.8')


if __name__ == "__main__":
    main()
