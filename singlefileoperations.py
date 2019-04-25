import cv2
import numpy as np

def nothing(x):
    pass;

cv2.namedWindow("input", cv2.WINDOW_GUI_EXPANDED)
cv2.createTrackbar('d','input',15,25,nothing)
cv2.createTrackbar('sigmaColour','input',155,255,nothing)
# cv2.namedWindow("grey", cv2.WINDOW_GUI_EXPANDED)
# cv2.namedWindow("thresholded", cv2.WINDOW_GUI_EXPANDED)

img = cv2.imread('33.JPG')
cv2.imshow("input", img)
# cv2.split(img,BGRChannels)
# BGRChannels[0]=cv2.zeros(img.shape[0],img.shape[1],CV_8UC1)
# cv2.merge(BGRChannels,3,img_noblue)
img_noblue = img[:,:,1]
# img_noblue[:,:,1] = img[:, :, 1] + 255 * np.ones((img.shape[0],img.shape[1]))


# img_lab = cv2.cvtColor(img, cv2.COLOR_BGR2LAB)
# cv2.imshow("processed", img_noblue)
cv2.namedWindow("R", cv2.WINDOW_GUI_EXPANDED)
cv2.namedWindow("G", cv2.WINDOW_GUI_EXPANDED)
cv2.namedWindow("B", cv2.WINDOW_GUI_EXPANDED)
cv2.imshow("R", img[:,:,2])
cv2.imshow("G", img[:,:,1])
cv2.imshow("B", img[:,:,0])
cv2.waitKey(0)
