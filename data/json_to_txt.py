import os
import subprocess
import json
import datetime

print(os.getcwd())

# create annotations file
file_path = "../keras-frcnn/"
file_name = "annotations_" + datetime.datetime.now().strftime("%Y-%m-%d_%H:%M:%S") + ".txt"
print(file_path, file_name)
annotations = open(file_path + file_name, "w+")

# save annotations to file
for r, d, f in os.walk("./"):
    for file in f:
        if '.json' in file:
            with open(file) as json_file:
                data = json.load(json_file)
                image_name = os.path.splitext(file)[0]
                image_path = os.getcwd() + "/" + image_name + ".jpg"
                for shape in data["shapes"]:
                    annotations.write(image_path + ",")
                    for point in shape["points"]:
                        for val in point:
                            annotations.write(str(val) + ",")
                    annotations.write("corn\n")

annotations.close()
