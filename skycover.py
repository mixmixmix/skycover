import glob
import cv2

def nothing(x):
    pass

img_dir = "./data/"
img_regex = "*.JPG"

img_list = glob.glob(img_dir + img_regex)
print(img_list)

cv2.namedWindow("input", cv2.WINDOW_GUI_EXPANDED)
cv2.createTrackbar('d','input',15,25,nothing)
cv2.createTrackbar('sigmaColour','input',155,255,nothing)
cv2.namedWindow("processed", cv2.WINDOW_GUI_EXPANDED)
cv2.namedWindow("grey", cv2.WINDOW_GUI_EXPANDED)
cv2.namedWindow("thresholded", cv2.WINDOW_GUI_EXPANDED)


for img_file in img_list:
    print('Opening: ' + img_file)
    img = cv2.imread(img_file)
    split_fname = img_file.split('.')[0:-1]
    split_fname.append("thresholded")
    split_fname.append("JPG")
    img_file_out = '.'.join(split_fname)
    cv2.imshow("input", img)

    while(1):
        k = cv2.waitKey(40)
        print(k)
        if k == 110:
            break
        d = cv2.getTrackbarPos('d','input')
        sigmaColour = cv2.getTrackbarPos('sigmaColour','input')
        d = cv2.getTrackbarPos('d','input')
        # img_blurred = cv2.bilateralFilter(img,d,sigmaColour,sigmaColour)
        img_grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        img_thresholded = cv2.adaptiveThreshold(img_grey,255,cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY,11,2)
        ret, img_thresholded = cv2.threshold(img_grey,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
        #display:
        # cv2.imshow("processed", img_blurred)
        # cv2.imshow("grey", img_grey)
        # cv2.imshow("thresholded", img_thresholded)
        print('Saving to: ' + img_file_out)
        cv2.imwrite(img_file_out,img_thresholded)
        break;

    # depressedKey = cv2.waitKey(0)
