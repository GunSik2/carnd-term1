#importing some useful packages
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
import cv2
import math
import os

def show():
    image = mpimg.imread('test_images/solidWhiteRight.jpg')

    # printing out some stats and plotting
    print('This image is:', type(image), 'with dimensions:', image.shape)
    plt.imshow(image)


def grayscale(img):
    return cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)



def canny(img, low_threshold, high_threshold):
    """Applies the Canny transform"""
    return cv2.Canny(img, low_threshold, high_threshold)


def gaussian_blur(img, kernel_size):
    """Applies a Gaussian Noise kernel"""
    return cv2.GaussianBlur(img, (kernel_size, kernel_size), 0)


def region_of_interest(img, vertices):
    # defining a blank mask to start with
    mask = np.zeros_like(img)

    # defining a 3 channel or 1 channel color to fill the mask with depending on the input image
    if len(img.shape) > 2:
        channel_count = img.shape[2]  # i.e. 3 or 4 depending on your image
        ignore_mask_color = (255,) * channel_count
    else:
        ignore_mask_color = 255

    # filling pixels inside the polygon defined by "vertices" with the fill color
    cv2.fillPoly(mask, vertices, ignore_mask_color)

    # returning the image only where mask pixels are nonzero
    masked_image = cv2.bitwise_and(img, mask)
    return masked_image


def draw_lines(img, lines, color=[255, 0, 0], thickness=2):
    leftLane = get_Lanes(lines, isLeft=True)
    leftLane = extend_Lane(leftLane, img.shape)

    rightLane = get_Lanes(lines, isLeft=False)
    rightLane = extend_Lane(rightLane, img.shape)

    lanelines = [leftLane, rightLane]

    for line in lanelines:
        if len(line) > 0:
            for x1, y1, x2, y2 in [line]:
                cv2.line(img, (x1, y1), (x2, y2), color, thickness)


# Find valid lines in the slope 10 to 80 degree line
def get_Lanes(lines, isLeft):
    slope_10 = math.pi / 18
    min_slope = math.tan(slope_10)  # 10 degree
    max_slope = math.tan(slope_10 * 8)  # 80 degree

    validLanes = []
    for line in lines:
        x1, y1, x2, y2 = line[0]
        slope = (y2 - y1) / (x2 - x1)
        validSlope = isValidSlope(slope, isLeft)
        if validSlope:
            validLanes.append(line[0])

    return validLanes


# Extend left and right lane
def extend_Lane(lines, shape):
    points = np.array(lines)
    if points.size == 0:
        return []

    xes = np.ndarray.flatten(points[:, 0:4:2])
    yes = np.ndarray.flatten(points[:, 1:4:2])
    slope, intercept = np.polyfit(xes, yes, 1)

    ex2 = shape[1]
    ey2 = slope * ex2 + intercept

    return list(map(int, [0, intercept, ex2, ey2]))


def isValidSlope(slope, isLeft):
    slope_10 = math.pi / 18
    min_slope = math.tan(slope_10)  # 10 degree
    max_slope = math.tan(slope_10 * 8)  # 80 degree

    if isLeft:
        return (min_slope <= slope <= max_slope)
    return (-max_slope <= slope <= -min_slope)


def hough_lines(img, rho, theta, threshold, min_line_len, max_line_gap):
    lines = cv2.HoughLinesP(img, rho, theta, threshold, np.array([]), minLineLength=min_line_len,
                            maxLineGap=max_line_gap)
    line_img = np.zeros((img.shape[0], img.shape[1], 3), dtype=np.uint8)
    draw_lines(line_img, lines)
    return line_img


# Python 3 has support for cool math symbols.
def weighted_img(img, initial_img, α=0.8, β=1., λ=0.):
    return cv2.addWeighted(initial_img, α, img, β, λ)


def findLane(initial_img):
    img = np.copy(initial_img)
    img = grayscale(img)
    img = canny(img, low_threshold=50, high_threshold=150)
    img = gaussian_blur(img, kernel_size=3)

    imshape = img.shape
    vertices = np.array([[(0, imshape[0]), (450, 330), (530, 330), (imshape[1], imshape[0])]], dtype=np.int32)
    img = region_of_interest(img, vertices)

    img = hough_lines(img, rho=2, theta=np.pi / 180, threshold=50, min_line_len=100, max_line_gap=160)
    img = region_of_interest(img, vertices)
    img = weighted_img(img, initial_img, α=0.8, β=1., λ=0.)

    return img


def imshow(img, gray=True, title=""):
    plt.figure()
    if not title:
        plt.title(title)
    if gray:
        plt.imshow(img, cmap='gray')
    else:
        plt.imshow(img)
    plt.show()

def show_images():
    for file in os.listdir("test_images/"):
        img = mpimg.imread("test_images/" + file)
        img = findLane(img)
        imshow(img, title=file)
        mpimg.imsave("test_images_output/" + file, img)

from moviepy.editor import VideoFileClip
from IPython.display import HTML

def process_image(image):
    result = findLane(image)
    return result

def show_videos_solidWhiteRight():
    white_output = 'test_videos_output/solidWhiteRight.mp4'
    clip1 = VideoFileClip("test_videos/solidWhiteRight.mp4")
    white_clip = clip1.fl_image(process_image)  # NOTE: this function expects color images!!
    white_clip.write_videofile(white_output, audio=False)

def show_videos_solidYellowLeft():
    yellow_output = 'test_videos_output/solidYellowLeft.mp4'
    clip2 = VideoFileClip('test_videos/solidYellowLeft.mp4')
    yellow_clip = clip2.fl_image(process_image)
    yellow_clip.write_videofile(yellow_output, audio=False)

def show_videos():
    challenge_output = 'test_videos_output/challenge.mp4'
    clip2 = VideoFileClip('test_videos/challenge.mp4')
    challenge_clip = clip2.fl_image(process_image)
    challenge_clip.write_videofile(challenge_output, audio=False)

#show_images()
#show_videos_solidWhiteRight()
show_videos()
