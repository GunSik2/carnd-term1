import numpy as np
import matplotlib.image as mpimg
import matplotlib.pyplot as plt

x = [1, 2, 3]
x.extend([4, 5])
x.extend('abc')
print(x)


def averge():
    x = [[1, 2, 3, 4], [5, 6, 7, 8]]
    npx = np.array(x)

    print("xes = ", npx[:, 0::2])
    print("flatten = ", np.ndarray.flatten(npx[:, 0::2]))
averge()

def test_append():
    xes = []
    xes.append([1, 2, 3, 4])
    xes.append([1, 2, 3, 4])
    print(xes)
test_append()

def test_extend():
    xes = [1, 2, 3]
    xes.extend([4])
    xes.extend([5])
    xes.extend([5])
    print(xes)
    print(int(sum(xes) / len(xes)))

test_extend()

def map_test():
    ev2 = [0, -655.93684210526317, 960, -1353.2]
    m2 = list(map(int, ev2))
    print(m2, ", ", ev2)

map_test()

def test():
    xy = [[2, 3, 3, 4]]
    x = xy[0]
    y = xy[0]
    print("x=", xy[0][0], ", y=", xy[0][2])

   # print("x=", x[0, 2], ", y=", y[1, 3])

test()

a = 1.
b = 3.
if a < b:
    print("a < b", "True")

na = np.array([1, 2, 3])
print(na, ", ", type(na), ", ", na.shape)

na = np.array([range(3), range(3)])
print(na, ", ", type(na), ", ", na.shape)


#reading in an image
image = mpimg.imread('../p1-LaneLines/test_images/solidWhiteRight.jpg')
print("shape=", image.shape)
print("image.shape[0]", image.shape[0])
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