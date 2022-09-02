import cv2
import numpy as np

def fun(a):
    pass

path = "resources/lamborgini.jpg"

cv2.namedWindow("Range Values")
cv2.resizeWindow("Range Values", 640, 240)
cv2.createTrackbar("Hue lower", "Range Values", 22, 179, fun)
cv2.createTrackbar("Hue upper", "Range Values", 94, 179, fun)
cv2.createTrackbar("Sat lower", "Range Values", 145, 255, fun)
cv2.createTrackbar("Sat upper", "Range Values", 255, 255, fun)
cv2.createTrackbar("Val lower", "Range Values", 88, 255, fun)
cv2.createTrackbar("Val upper", "Range Values", 255, 255, fun)

while True:
    img = cv2.imread(path)
    img = cv2.resize(img, (300,200))
    HSV_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    h_lower = cv2.getTrackbarPos("Hue lower", "Range Values")
    h_upper = cv2.getTrackbarPos("Hue upper", "Range Values")
    s_lower = cv2.getTrackbarPos("Sat lower", "Range Values")
    s_upper = cv2.getTrackbarPos("Sat upper", "Range Values")
    v_lower = cv2.getTrackbarPos("Val lower", "Range Values")
    v_upper = cv2.getTrackbarPos("Val upper", "Range Values")
    #print(h_lower, h_upper, s_lower, s_upper, v_lower, v_upper)
    lower = np.array([h_lower, s_lower, v_lower])
    upper = np.array([h_upper, s_upper, v_upper])
    mask = cv2.inRange(HSV_img, lower, upper)
    mask_RGB = cv2.cvtColor(mask, cv2.COLOR_GRAY2BGR)
    result_img = cv2.bitwise_and(img, img, mask = mask)

    h_stack = np.hstack((img, HSV_img, mask_RGB, result_img))
    cv2.imshow("All images", h_stack)
    # cv2.imshow("Original image", img)
    # cv2.imshow("HSV image", HSV_img)
    # cv2.imshow("Mask", mask)
    # cv2.imshow("Result", result_img)

    cv2.waitKey(1)

