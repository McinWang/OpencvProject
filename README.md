
# Introduction
##### This repository is used to record some projects tried in the process of learning opencv.

##### Code is not 100% original, part of the code from the network (From Github,CSDN...)

##### `use_camera.py` Using opencv to call the local camera

##### `hand_detection.py` Estimated the pose(Consists all keypoints and their connecting relationships) of hands in the picture

##### `gesture_recognition.py` Detecting the simple gesture of only one hand in an image (including:'zero','one','two','three','four','five','six','eight','thumbup','**'

##### `face_detection.py` Detect all the faces that appear on the screen and frame them for display

##### `face_recognition.py` Estimated the face (also include the left/right hand and whole body can chose)  in the picture


## Installation
##### Clone this repo, and we'll call the directory that you cloned as ${OPENCV_ROOT}.

#### Create a new conda environment (optional)
`conda create -n {your_env_name} python={x.x}`

#### Install opencv-python, mediapipe
`pip install opencv-python mediapipe`  

## Usage
##### Enter `python X.py` to start
##### When the camera is working, press the ‘q’ key on the keyboard to end the process。
