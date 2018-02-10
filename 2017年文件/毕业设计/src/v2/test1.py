import cv2
import numpy as np 
import matplotlib.pyplot as plot
img = cv2.imread('1.jpg');
hullIndex = cv2.convexHull(img, returnPoints = False)

output = cv2.seamlessClone(src, dst, mask, center, cv2.NORMAL_CLONE)
cv2.imshow("EmptyImage3", output)
print img
cv2.waitKey (0)
cv2.destroyAllWindows()
