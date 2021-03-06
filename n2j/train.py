"""Training various models.
This script trains a model according to the config specifications.

Example
-------
To run this script, pass in the path to the user-defined training config file as the argument::

    $ python ex-con/train.py ex-con/example_user_config.py

"""

import os, sys
import random
import argparse
from addict import Dict
import numpy as np # linear algebra
from tqdm import tqdm
# torch modules
import torch
import torch.optim as optim
from torch.utils.data import DataLoader
from torch.utils.tensorboard import SummaryWriter
# h0rton modules
'''
from h0rton.trainval_data import XYData
from h0rton.configs import TrainValConfig
import h0rton.losses
import h0rton.models
import h0rton.h0_inference
import h0rton.train_utils as train_utils
'''


def parse_args():
    """Parse command-line arguments
    """
    pass

def seed_everything(global_seed):
    """Seed everything for reproducibility

    global_seed : int
        seed for `np.random`, `random`, and relevant `torch` backends


    """
    pass


def main():
    pass

if __name__ == '__main__':
    main()
