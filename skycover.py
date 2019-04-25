""""
Uses Otsu thresholding (adapitve based on histogram assuming bi-modal distribution of pixel intensities) on blue channel to generate a black and white image. The blue channel has the best contrast between sky and other objects. Then it uses morphological erosion (expands black areas) to account for lost coverage due to fact that images are taken against the light source so edges are naturally overexposed.

"""
import glob
import cv2
import numpy as np

def nothing(x):
    pass

img_dir = "./data/"
img_regex = "*.JPG"

img_list = glob.glob(img_dir + img_regex)

morph_kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(5,5))

cv2.namedWindow("input", cv2.WINDOW_GUI_EXPANDED)
cv2.namedWindow("grey", cv2.WINDOW_GUI_EXPANDED)
cv2.namedWindow("thresholded", cv2.WINDOW_GUI_EXPANDED)


for img_file in img_list:
    img = cv2.imread(img_file)
    split_fname = img_file.split('.')[0:-1]
    split_fname.append("thresholded")
    split_fname.append("JPG")
    img_file_out = '.'.join(split_fname)
    cv2.imshow("input", img)
    height = img.shape[0]
    width = img.shape[1]
    noPixels = height * width


    img_grey = img[:,:,0]#Blue channel has the best contrast of colours for us
    ret, img_thresholded = cv2.threshold(img_grey,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
    img_thresholded_morph = cv2.erode(img_thresholded, morph_kernel, iterations = 2)
    img_fin = img_thresholded_morph
    img_thresh_disp = cv2.cvtColor(img_fin, cv2.COLOR_GRAY2BGR)

    #Saving pair of original and thresholded
    img_pair = np.concatenate((img, img_thresh_disp), axis=1)
    cv2.imwrite(img_file_out,img_pair)

    #Calculate percentage of sky covered
    ones = cv2.countNonZero(img_fin)
    coverage = 100 * (1 - ones/noPixels)
    print("{0} , {1:.2f} ".format(img_file,coverage ))

    # depressedKey = cv2.waitKey(0) #uncomment to show images for longer time
