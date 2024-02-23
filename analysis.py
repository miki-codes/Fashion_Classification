from keras.optimizers import Adam
from keras.preprocessing.image import img_to_array
import keras.models
from keras.optimizers.schedules import ExponentialDecay
from sklearn.preprocessing import LabelBinarizer
from sklearn.model_selection import train_test_split
from pyimagesearch.fashionnet import FashionNet
from imutils import paths
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import argparse
import random
import pickle
import cv2
import os

history = pickle.load(open('history.pkl', 'rb'))
print(history)

