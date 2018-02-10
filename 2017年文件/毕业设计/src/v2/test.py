import cv2
import numpy as np 
import matplotlib.pyplot as plot
img = cv2.imread('img/0.jpg');
hsv_roi =  cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
mask = cv2.inRange(hsv_roi, np.array((0., 60.,32.)), np.array((180.,255.,255.)))
roi_hist = cv2.calcHist([hsv_roi],[0],mask,[180],[0,180])
d = cv2.compareHist( roi_hist,roi_hist, cv2.CV_COMP_INTERSECT)
img = cv2.compareHist([img],[0],roi_hist,[0,180],1)
cv2.imshow("EmptyImage3", img)
print img
cv2.waitKey (0)
cv2.destroyAllWindows()
