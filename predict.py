# Python script for inferencing images on model
import os
import argparse
import cv2

# initiate the parser
parser = argparse.ArgumentParser()
parser.add_argument("-inputs", help="Input folder of images")
args = parser.parse_args()

intro = "\n\n*************************\n*                       *\n*    Welcome to corn    *\n*      or not corn!     *\n*                       *\n*************************\n"
print(intro)

ls = os.listdir(args.inputs)
ls = [f for f in ls if os.path.isfile(os.path.join(args.inputs,f))]

print("These files will be labelled:")
print(ls)

# Create output directory
try:
    os.mkdir("output_data")
except OSError:
    print("Either your output_data folder already exists, or it broke.")

print("\n ***********************")
print(" *      Labelling      *")
print(" ***********************\n")

for img_file in ls:
    img = cv2.imread(os.path.join(args.inputs,img_file))
    status = cv2.imwrite(os.path.join("output_data",img_file),img)
    print(" > Labelled '"+img_file+"'")
