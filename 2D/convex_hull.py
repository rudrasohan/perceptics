import cv2
import numpy as np
import sys

folder = sys.argv[1]
filename = folder + "/image.png"
img = cv2.imread(filename)
img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(img_gray, 127, 255, 1)
im2, contours,hierarchy = cv2.findContours(thresh,2,1)

cnt = contours[0]

hull = cv2.convexHull(cnt)

for i in range(hull.shape[0]-1):
    start = (hull[i][0][0], hull[i][0][1])
    end = (hull[i+1][0][0], hull[i+1][0][1])
    cv2.line(img,start,end,[0,255,0],2)

cv2.line(img, (hull[0][0][0], hull[0][0][1]), (hull[hull.shape[0]-1][0][0],
	hull[hull.shape[0]-1][0][1]), [0,255,0],2)
cv2.imshow('img',img)
cv2.waitKey(0)
cv2.destroyAllWindows()