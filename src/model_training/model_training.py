
import os
import argparse
import json
from tensorflow.keras.utils import set_random_seed
from tensorflow import keras
from tensorflow.keras import layers

parser = argparse.ArgumentParser()
parser.add_argument("config_path", type=str)
args = parser.parse_args()
with open(args.config_path, "r") as f:
    config = json.load(f)

set_random_seed(config['random_seed'])
num_choices = config['num_choices']
print(num_choices)
print("lol")



