# Python script for inferencing images on model

import argparse

# initiate the parser
parser = argparse.ArgumentParser()
parser.add_argument("-inputs", help="Input folder of images")
args = parser.parse_args()

intro = "*************************\n*                       *\n*    Welcome to corn    *\n*      or not corn!     *\n*                       *\n*************************"

print(args.inputs)
