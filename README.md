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
+-- png
|   +-- 2ft
|   |   +-- GOPRO165
|   |   |   +-- GOPRO16501.png
|   |   |   +-- GOPRO16502.png
|   |   |       ...
|   |   +-- GOPRO166
|   |   |   +-- GOPRO16601.png
|   |   |   +-- GOPRO16602.png
|   |   |       ...
|   |       ...
|   +-- 4ft
|   |   +-- GOPRO388
|   |   |   +-- GOPRO38801.png
|   |   |   +-- GOPRO38802.png
|   |   |       ...
|   |   +-- GOPRO389
|   |   |   +-- GOPRO38901.png
|   |   |   +-- GOPRO38902.png
|   |   |       ...
|   |       ...
```

## How to Train

At path `~/corn/keras-frcnn/` run:

`python train_frcnn.py -o simple -p training/example_labels.txt`


## How to Inference

At path `~/corn/inference/` run:

`predict.py -inputs=<path_to_inputs>`

Inputs should be a folder of images to label.

Output images will automatically be saved to an "outputs" folder.

## Tools

- [VGG Image Annotator (VIA)](www.robots.ox.ac.uk/~vgg/software/via/)
- [keras-frcnn](https://github.com/kbardool/keras-frcnn)
