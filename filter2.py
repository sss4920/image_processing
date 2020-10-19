import cv2
import matplotlib.pyplot as plt
import numpy as np

image = cv2.imread('test.png')
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.show()

size = 4
kernel = np.ones((size,size), np.float32) / (size**2) # 4*4짜리 커널을 16분의 1이라는 값으로 모두 넣음
print(kernel)
# 직접만들어서 커널안쓰고 cv2.blur쓰면 자동으로 커널 만들수잇음




dst = cv2.filter2D(image, -1, kernel) # 모든 픽셀을 다 커널을 이용하여 그 결과를 저장
plt.imshow(cv2.cvtColor(dst, cv2.COLOR_BGR2RGB))
plt.show()