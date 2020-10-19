import cv2 as cv

img_color = cv.imread('sss.jpg')
img_gray = cv.cvtColor(img_color, cv.COLOR_BGR2GRAY)
ret, img_binary = cv.threshold(img_gray, 127, 255, 0)



contours, hierachy = cv.findContours(img_binary, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)

img_canny = cv.Canny(img_gray, 50, 150)
cv.drawContours(img_canny, contours, -1, (0,255,0),3)
cv.imshow("Canny Edge", img_canny)
cv.imshow("result", img_color)
cv.waitKey(0)