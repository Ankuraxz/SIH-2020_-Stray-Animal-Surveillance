import os
import sys
# next line to be sorted: Env setup using ProtoBuf
sys.path.append('/Users/Dell/AppData/Local/Programs/Python/Python37/Lib/site-packages')
# ref: https://developers.google.com/protocol-buffers
# pip install tensorflow
# pip install pillow
# pip install numpy
# pip install opencv-python

import tensorflow as tf
import os

graph_def = tf.compat.v1.GraphDef()
labels = []

# These are set to the default names from exported models, update as needed.
filename = "model.pb" #tf model.pb
labels_filename = "labels.txt" #labels .txt/.pbtxt{Pref.}

# Import the TF graph
with tf.io.gfile.GFile(filename, 'rb') as f:
    graph_def.ParseFromString(f.read())
    tf.import_graph_def(graph_def, name='')

# Create a list of labels.
with open(labels_filename, 'rt') as lf:
    for l in lf:
        labels.append(l.strip())

#PREDICTION IMAGE PROCESSING

from PIL import Image #pillow
import numpy as np
import cv2

# Load from a file
imageFile = "<path to your image file>" # test Image path
image = Image.open(imageFile)

# Update orientation based on EXIF tags, if the file has orientation info.
image = update_orientation(image)

# Convert to OpenCV format
image = convert_to_opencv(image)
