import os
import subprocess

fps = "1"

for r, d, f in os.walk("./"):
    for file in f:
        if '.png' in file:
            name = os.path.splitext(file)[0]
            print("Name: ", name, "  file: ", file)

            # create directory
            #try:
            #    os.mkdir("jpg")
            #except FileExistsError:
            #    print("Directory 'jpg' already exists")

            # generate image sequence and save to directory
            #command = "ffmpeg -i " + name + ".MP4 -vf fps=" + fps + " " + name + "/" + name + "%02d.jpg"

            #output = os.system(command)
            #print(output)
