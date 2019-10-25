# corn
Predict corn.

## Data

```
.
+-- example_labels
|   +-- Label Demo - 1.png
|   +-- Label Demo - 2.png
|   +-- ...
+-- mp4
|   +-- 2ft
|   |   +-- GOPRO165.MP4
|   |   +-- GOPRO166.MP4
|   |       ...
|   +-- 4ft
|   |   +-- GOPRO388.MP4
|   |   +-- GOPRO389.MP4
|   |       ...
+-- jpg
|   +-- GOPRO165_01.jpg
|   +-- GOPRO165_02.jpg
|       ...
|   +-- GOPRO166_01.jpg
|   +-- GOPRO166_02.jpg
|       ...
|   +-- GOPRO388_01.jpg
|   +-- GOPRO388_02.jpg
|       ...
|   +-- GOPRO389_01.jpg
|   +-- GOPRO389_02.jpg
|       ...
```

## How to Train

At path `~/corn/keras-frcnn/` run:

`python train_frcnn.py -o simple -p example_annotations.txt`

Note: `example_annotations.txt` seems to only work with absolute paths. I used absolute paths for my system, but obviously this won't work for others.

TODO: Create a "base_annotations.txt" with relative paths and a Python script that converts relative paths to absolute paths given a "base path".
- e.g. converts 'path/to/file.jpg' to '/home/zbalda/path/to/file.jpg' for base path "home/zbalda/"

## How to Inference

At path `~/corn/inference/` run:

`predict.py -inputs=<path_to_inputs>`

Inputs should be a folder of images to label.

Output images will automatically be saved to an "outputs" folder.

## Tools

- [labelme](https://github.com/wkentaro/labelme)
- [keras-frcnn](https://github.com/kbardool/keras-frcnn)
- [FFmpeg](https://www.ffmpeg.org/)
