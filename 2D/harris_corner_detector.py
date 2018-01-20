import cv2
import numpy as np

import sys

"""Pass folder of environment as command line argument """

folder = sys.argv[1]
filename = folder + "/image.png"
img = cv2.imread(filename)
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

gray = np.float32(gray)
dst = cv2.cornerHarris(gray,2,3,0.04)

#result is dilated for marking the corners, not important
#dst = cv2.dilate(dst,None)

# Threshold for an optimal value, it may vary depending on the image.
img[dst>0.4*dst.max()]=[0,0,255]
max_val = dst.max()
height, width = dst.shape
points = []
for i in range(height):
	for j in range(width):
		if(dst[i,j]>0.4*max_val):
			points.append((i,j))

print points #array to store the points extracted by harris

cv2.imshow('dst',img)
if cv2.waitKey(0) & 0xff == 27:
    cv2.destroyAllWindows()
