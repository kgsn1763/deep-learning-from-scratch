#!/usr/bin/env python
# coding: utf-8

import os
import matplotlib.pyplot as plt
from matplotlib.image import imread

img = imread(os.path.dirname(os.path.abspath(__file__)) + '/../dataset/lena.png')  # 画像の読み込み
plt.imshow(img)

plt.show()
