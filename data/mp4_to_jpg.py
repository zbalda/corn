import os
import subprocess

fps = "1"

# create directory
try:
    os.mkdir("jpg")
except FileExistsError:
    print("Directory 'jpg' already exists")

for r, d, f in os.walk("./"):
    for file in f:
        if '.MP4' in file:
            name = os.path.splitext(file)[0]

            # generate image sequence and save as jpg images
            command = "ffmpeg -i " + file + " -vf fps=" + fps + " " + name + "_%02d.jpg"
            output = os.system(command)
            print(output)
