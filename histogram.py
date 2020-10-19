import cv2
import numpy as np

src = cv2.imread("road.jpg")
gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
result = np.zeros((src.shape[0], 256), dtype=np.uint8)
result1 = np.zeros((src.shape[0], 256), dtype=np.uint8)
result2 = np.zeros((src.shape[0], 256), dtype=np.uint8)

hist = cv2.calcHist([src], [0], None, [256], [0, 256])
hist2 = cv2.calcHist([src], [1], None, [256], [0, 256])
hist3 = cv2.calcHist([src], [2], None, [256], [0, 256])


cv2.normalize(hist, hist, 0, result.shape[0], cv2.NORM_MINMAX)
cv2.normalize(hist2, hist2, 0, result1.shape[0], cv2.NORM_MINMAX)
cv2.normalize(hist3, hist3, 0, result2.shape[0], cv2.NORM_MINMAX)


for x, y in enumerate(hist):
    print("b",x,y)
    cv2.line(result, (x, result.shape[0]), (x, result.shape[0] - y), 255)

for x, y in enumerate(hist2):
    print("g",x,y)
    cv2.line(result1, (x, result.shape[0]), (x, result.shape[0] - y), 255)

for x, y in enumerate(hist3):
    print("r",x,y)
    cv2.line(result2, (x, result.shape[0]), (x, result.shape[0] - y), 255)
dst = np.hstack([result, result1,result2])

cv2.imshow("dst", dst)
cv2.imshow("result",result1)
cv2.imshow("result1",result2)
cv2.waitKey(0)
cv2.destroyAllWindows()