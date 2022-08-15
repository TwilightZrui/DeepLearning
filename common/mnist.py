# coding: utf-8
try:
    import urllib.request 
except ImportError:
    rais Import('should use Python 3.x')
from cProfile import label
import os.path
import gzip
import pickle
import os
import numpy as np 

url_base = 'http://yann.lecun.com/exdb/mnist/'
key_file = {
    'train_img':'train-images-idx3-ubyte.gz',
    'train_label':'train-labels-idx1-ubyte.gz',
    'test_img':'t10k-images-idx3-ubyte.gz',
    'test_label':'t10k-labels-idx1-ubyte.gz'
}

dataset_dir = os.path.dirname(os.path.abspath(__file__))
save_file = dataset_dir + "/mnist.pkl"

train_num = 60000
test_num = 10000
img_dim = (1,28,28)
img_size = 784 

def _download(file_name):
    file_path = dataset_dir + "/" +file_name
    if os.path.exists(file_name):
        return 
    print("Downloading " + file_name + "...")
    urllib.request.urlretrieve(url_base + file_name, file_path)
    print("Done")

def download_mnist():
    for v in key_file.values():
        _download(v)

def _load_lable(file_name):
    file_path = dataset_dir + "/" + file_name

    print("Converting  " + file_name + "to Numpy Array ...")

    with gzip.open(file_name, 'rb') as f:
        labels = np.frombuffer(f.read(), np.uint8, offset=8)
    print("Done")

    return labels

def _load_img(file_name):
    file_path = dataset_dir + "/" + file_name
    print("Converting " + file_name + " to Numpy Array...")
    with gzip.open(file_path, 'rb') as f:
        data = np.frombuffer(f.read(), np.uint8, offset=16)
        data = data.reshape(-1, img_size)
        print("Done")
    return data
        