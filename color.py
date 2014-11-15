import numpy as np
import cv2

webcam = cv2.VideoCapture(0)

if webcam.isOpened(): # try to get the first frame
    rval, image = webcam.read()
else:
    rval = False

# define the list of acceptable colors
colors = [([0, 0, 0], [255, 155, 255])]

while rval:
        # loop over the boundaries
        for (lower, upper) in colors:
                # create NumPy arrays from the boundaries
                lower = np.array(lower, dtype = "uint8")
                upper = np.array(upper, dtype = "uint8")
         
                # find the colors within the specified boundaries and apply
                # the mask
                mask = cv2.inRange(image, lower, upper)
                output = cv2.bitwise_and(image, image, mask = mask)
         
                # show the images
                cv2.imshow("images", np.hstack([image, output]))
        rval, image = webcam.read()
        
        key = cv2.waitKey(20)
        if key in [27, ord('Q'), ord('q')]: # exit on ESC
                cv2.destroyWindow("images")
                break
