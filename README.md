# Image2Cartoon
Convert a given image to a cartoon using **Python** and **OpenCV**

## Input image

<p align="center">
  <img width="250" alt="Original Lena Image" src="https://user-images.githubusercontent.com/72186725/146640563-f6350add-7d00-43e2-9239-c2b68a185c50.png">
  <br>
  <em>The Lena Image</em>
</p>

## Output images

<p align="center">
  <img width="300" alt="Screenshot 2021-12-18 at 17 41 52" src="https://user-images.githubusercontent.com/72186725/146640777-e2525703-aba9-4bf6-8044-5a8f3ab7e90e.png">
  <br>
  <em>Original Image</em>
</p>

<p align="center">
<img width="330" alt="Screenshot 2021-12-18 at 17 41 58" src="https://user-images.githubusercontent.com/72186725/146640808-779409fd-d2a9-44c8-9659-da6cbdd40659.png">
  <br>
  <em>Image with edges only</em>
</p>

<p align="center">
  <img width="300" alt="Screenshot 2021-12-18 at 17 41 55" src="https://user-images.githubusercontent.com/72186725/146640853-5e2deea8-a86b-460e-ba1a-7a5a6f6f120a.png">

  <br>
  <em>Cartoonised image</em>
</p>

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
