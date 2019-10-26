# corn
Predict corn.

## Data

```
.
+-- data
|   +-- GOPRO165_01.jpg
|   +-- GOPRO165_01.json
|   +-- GOPRO165_02.jpg
|   +-- GOPRO165_02.json
|       ...
|   +-- GOPRO165.MP4
|   +-- GOPRO166_01.jpg
|   +-- GOPRO166_01.json
|       ...
|   +-- GOPRO166_18.jpg
|   +-- GOPRO166_18.json
|   +-- GOPRO166.MP4
|       ...
|       ...
```

To generate JPG

## How to Train

At path `~/keras-frcnn/` run:

`python train_frcnn.py -o simple -p annotations.txt`

Note: replace annotations.txt with actual annotations file

## How to Inference

At path `~/inference/` run:

`predict.py -inputs=<path_to_inputs>`

Inputs should be a folder of images to label.

Output images will automatically be saved to an "outputs" folder.

## Converting JSON Annotations to .txt Format

Annotations were done with [labelme](https://github.com/wkentaro/labelme) which saves a json file for each annotated image (at `/data/`). The keras-frcnn model accepts a single .txt file which has a specific format. To generate a single .txt file from the json files, navigate to `~/data/` and run the script we created:

`python json_to_txt.py`

## Tools

- [labelme](https://github.com/wkentaro/labelme)
- [keras-frcnn](https://github.com/kbardool/keras-frcnn)
- [FFmpeg](https://www.ffmpeg.org/)
