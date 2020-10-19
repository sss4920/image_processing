# 컨볼루션 계산 각각의 픽셀에 대해서 커널을 적용해 필터링을 함
# basic kernel 모두 같은가중치
# gausian kernel 모두 정규분포로 이루어진 가중치로 구성
# 직접 커널을 생성하여 필터 적용하기
import cv2
import numpy as np
import matplotlib.pyplot as plt

image = cv2.imread('test.png')
cv2.imshow('Image', image)
cv2.waitKey(0)

size = 4
kernel = np.ones((size,size), np.float32)/(size **2)
print(kernel)

dst = cv2.filter2D(image, -1, kernel)
cv2.imshow('Image', dst)
cv2.waitKey(0)