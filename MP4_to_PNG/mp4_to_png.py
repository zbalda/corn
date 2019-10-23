import os
import subprocess

fps = "1"

for r, d, f in os.walk("./"):
    for file in f:
        if '.MP4' in file:
            name = os.path.splitext(file)[0]
            print(name)

            # create directory
            try:
                os.mkdir(name)
            except FileExistsError:
                print("Directory " , name ,  " already exists")

            # generate image sequence and save to directory
            command = "ffmpeg -i " + name + ".MP4 -vf fps=" + fps + " " + name + "/" + name + "%02d.png"

            output = os.system(command)
            print(output)
