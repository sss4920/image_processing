# thresh_binary thresh보다 큰 값을 하얀색으로 바꿈 255로
import cv2
from PIL import Image
import matplotlib.pyplot as plt
import numpy as np
img = Image.open('신발(48).jpg')# 이미지 데이터 열기
img = img.convert('L')
plt.imshow(img, cmap='Greys_r')
plt.show()
pixel_data = img.getdata() #픽셀데이터 가져오기
pixels = np.array(pixel_data) # numpy 배열로 변환하기
gray = cv2.cvtColor(pixels, cv2.IMREAD_GRAYSCALE)
ret, thres = cv2.threshold(gray, 127, 255 , cv2.THRESH_BINARY)
plt.imshow(cv2.cvtColor(thres, cv2.COLOR_GRAY2RGB))
plt.show()
