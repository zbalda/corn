# corn
Predict corn.

#### Members

- Zachary Balda
- Brandon Boynton
- Laurent Valle

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

## How to Train

At path `/keras-frcnn/` run:

`python train_frcnn.py -o simple -p annotations.txt`

Note: replace annotations.txt with actual annotations file

## How to Inference

Place images in `/keras-frcnn/test_images/`

At path `/keras-frcnn/` run:

`python test_frcnn.py -p test_images`

Outputs are saved to `/keras-frcnn/results_images/`

Note: Images must be .jpg format


## Converting MP4 Videos to .jpg Image Sequences

The keras-frcnn model only accepts .jpg images. To convert MP4 videos to .jpg image sequences put all MP4 videos in `/data/` and run the script we created:

`python mp4_to_jpg.py`

Set `fps` in `mp4_to_jpg.py` to choose number of frames per second (default `1`)

## Converting JSON Annotations to .txt File

Annotations were done with [labelme](https://github.com/wkentaro/labelme) which saves a json file for each annotated image (at `/data/`). The keras-frcnn model accepts a single .txt file which has a specific format. To generate a single .txt file from the json files, navigate to `/data/` and run the script we created:

`python json_to_txt.py`

## Dependencies

- pandas
- matplotlib
- tensorflow
- keras – 2.0.3
- numpy
- opencv-python
- sklearn
- h5py

## Tools

- [labelme](https://github.com/wkentaro/labelme)
- [keras-frcnn](https://github.com/kbardool/keras-frcnn)
- [FFmpeg](https://www.ffmpeg.org/)
