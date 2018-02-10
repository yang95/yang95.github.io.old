import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('img/0.jpg',0)  
f = np.fft.fft2(img)
fshift = np.fft.fftshift(f) 


print img
print f
