import cv2 as cv

# Getting image
img = cv.imread("/Users/jahnaviyelamanchi/Projects/Screenshot 2021-11-14 at 08.58.16.png")

# Converting to gray scale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# Applying median blur
gray = cv.medianBlur(gray,5)

# Applying adaptive thresholding
edges = cv.adaptiveThreshold(gray,255,cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 9, 9)

# Applying bilateral filter
colour = cv.bilateralFilter(img,9,250,250)

# Compiling all images bit-by-bit
cartoon = cv.bitwise_and(colour,colour,mask=edges)

# Displaying images from 3 stages
cv.imshow("image",img)
cv.imshow("edges", edges)
cv.imshow("Cartoon", cartoon)

# Waiting for 0 milliseconds for a key press on a OpenCV window
cv.waitKey(0)

# To close all open windows simultaneously
cv.destroyAllWindows()
