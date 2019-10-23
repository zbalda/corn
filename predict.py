# Python script for inferencing images on model
import os
import argparse

# initiate the parser
parser = argparse.ArgumentParser()
parser.add_argument("-inputs", help="Input folder of images")
args = parser.parse_args()

intro = "\n\n*************************\n*                       *\n*    Welcome to corn    *\n*      or not corn!     *\n*                       *\n*************************\n"
print(intro)

ls = os.listdir(args.inputs)
ls = [os.path.join(args.inputs,f) for f in ls if os.path.isfile(os.path.join(args.inputs,f))]

print("Converting:")
print(ls)
