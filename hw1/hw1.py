import cv2
import numpy as np
import os
import torch
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
# %matplotlib inline

img_dir = "images_corrected"
if os.path.exists(img_dir):
    if not os.listdir(img_dir):
        print(f"No files in dir {img_dir}")
        exit(0)
    num_img = len(os.listdir(img_dir))
    for img in os.listdir(img_dir):
        if not img.endswith('.jpg'):
            continue
        img_path = os.path.join(img_dir, img)
        image = cv2.imread(img_path)
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        plt.imshow(gray)
        plt.show()
else:
    print(f"Image dir not found: {img_dir}")
    exit(0)
print('DONE')
