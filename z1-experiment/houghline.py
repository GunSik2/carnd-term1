import cv2
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.image as mpimg

initial_img = cv2.imread("../p1-LaneLines/test_images/test.jpg")
#initial_img = mpimg.imread("../p1-LaneLines/test_images/test.jpg")
def houghline(initial_img, low_threshold=60, high_threshold=180, minLineLength=40, maxLineGap=15):
    img = np.copy(initial_img)
    gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    edges = cv2.Canny(gray, low_threshold, high_threshold, apertureSize = 3)

    lines = cv2.HoughLinesP(edges, 2, np.pi/180, 15, minLineLength, maxLineGap)
    for line in lines:
        print("line=", type(line), ", ", line.shape, ", ", line)

        for x1,y1,x2,y2 in line:
            cv2.line(img,(x1,y1),(x2,y2),(0,255,0),2)
    return img

plt.figure()

for i in range(1, 5):
    print(i)
    img = houghline(initial_img, low_threshold=10 * i)
    plt.subplot(2, 4, i)
    plt.imshow(img, cmap='gray')
    plt.title(i)


for i in range(5, 9):
    print(i)
    img = houghline(initial_img, low_threshold=10 * i)
    plt.subplot(2, 4, i)
    plt.imshow(img, cmap='gray')
    plt.title(i)
plt.show()

#cv2.imwrite('houghlines5.jpg',img)
