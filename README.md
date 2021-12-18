# Image2Cartoon
Convert a given image to a cartoon using **Python** and **OpenCV**

## Steps involved

* Get cartoon effect
  1. Downscale the image
  2. Apply [bilateral filter](https://www.tutorialspoint.com/opencv/opencv_bilateral_filter.htm)
  3. upscale image

* Get blurred boundaries of original image
  1. Convert image to gray scale
  2. Apply [median blur filter](https://www.tutorialspoint.com/opencv/opencv_median_blur.htm#:~:text=The%20Median%20blur%20operation%20is,edges%20while%20removing%20the%20noise.)

* Identify edges & add to the image (to get a sketching effect)
  1. Use [adaptive thresholding](https://www.tutorialspoint.com/opencv/opencv_adaptive_threshold.htm#:~:text=Adaptive%20thresholding%20is%20the%20method,()%20of%20the%20Imgproc%20class.) / any type of thresholding
  2. Compile all images

## References

* [Cartooning an image](https://www.geeksforgeeks.org/cartooning-an-image-using-opencv-python/)
* [Adaptive thresholding](https://www.geeksforgeeks.org/python-thresholding-techniques-using-opencv-set-2-adaptive-thresholding/)
* [Image blurring](https://www.geeksforgeeks.org/python-image-blurring-using-opencv/)
* [Bilateral filtering](https://www.geeksforgeeks.org/python-bilateral-filtering/)
