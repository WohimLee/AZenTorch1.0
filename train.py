
import os
import sys
import yaml
import time
import torch
import random
import argparse
import subprocess

import numpy as np
import torch.distributed as dist

from pathlib import Path

from utils.args_parse import parse_opt


FILE = Path(__file__).resolve()
ROOT = FILE.parents[0]  # YOLOv5 root directory
if str(ROOT) not in sys.path:
    sys.path.append(str(ROOT))  # add ROOT to PATH
ROOT = Path(os.path.relpath(ROOT, Path.cwd()))  # relative


LOCAL_RANK = int(os.getenv('LOCAL_RANK', -1))  # https://pytorch.org/docs/stable/elastic/run.html
RANK       = int(os.getenv('RANK', -1))
WORLD_SIZE = int(os.getenv('WORLD_SIZE', 1))


def main(opt):
    pass



if __name__ == '__main__':
    opt = parse_opt()
    main(opt)