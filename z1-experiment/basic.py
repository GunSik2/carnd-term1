import numpy as np
import matplotlib.image as mpimg
import matplotlib.pyplot as plt

na = np.array([1, 2, 3])
print(na, ", ", type(na), ", ", na.shape)

na = np.array([range(3), range(3)])
print(na, ", ", type(na), ", ", na.shape)


#reading in an image
image = mpimg.imread('../p1-LaneLines/test_images/solidWhiteRight.jpg')
print(image.shape)
plt.imshow(image)
print(image[0, 0, :])



# Pi
print("np.pi = ", np.pi)
v = np.sin(np.pi)
print("np.sin(np.pi) = ", v)
v = np.sin(np.pi/180.)
print("np.pi/180 = ", v)
v = np.sin(np.pi/2)
print("np.pi/2 = ", v)