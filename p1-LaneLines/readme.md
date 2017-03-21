# **Finding Lane Lines on the Road** 
---

**Finding Lane Lines on the Road**

The goals / steps of this project are the following:
* Make a pipeline that finds lane lines on the road
* Reflect on your work in a written report


[org-image1]: ./test_images/solidWhiteCurve.jpg "solidWhiteCurve"
[out-image1]: ./test_images_output/solidWhiteCurve.jpg "solidWhiteCurve"
[image3]: ./test_images_output/solidWhiteRight.jpg "solidWhiteRight"

---

### Reflection

### 1. Describe your pipeline. As part of the description, explain how you modified the draw_lines() function.

My pipeline consisted of 5 steps:
1) converted the images to grayscale
2) extracted structural information using Canny edge detection
3) reduced image noise by appliying Gaussian blur 
4) reduced image range of interst by applying image mask
5) extracted left and right lines using probababilic hough lines

In order to draw a single line on the left and right lanes, I modified the draw_lines() function as follows:
1) separated the left and right lines by checking slope of each line.
   To minimize noise errors, I dropped out any line having slope below 10 degree or over 80 degree.
2) extended lane by finding the vector of coefficients that minimises the squared errors for all the points.  

Let's check how the pipeline works on the original image:

![alt text][org-image1]
![alt text][out-image1]


### 2. Identify potential shortcomings with your current pipeline

The pipeline based on several assumptions, and the lane detection can be broken if those are not fit:
1) The region of interest is fixed, so the lane line can be too long or short if a campera viewpoint is not correct.  
2) TBD


### 3. Suggest possible improvements to your pipeline

A possible improvement would be to ...

Another potential improvement could be to ...
