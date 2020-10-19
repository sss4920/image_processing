import cv2
import matplotlib.pyplot as plt

image = cv2.imread('test.png')
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.show()

#kernel size가 홀수가 되어야함 size가 커지면 블러링이 심해지고 작으면 블러링 약해짐
dst = cv2.GaussianBlur(image, (5,5), 0)
plt.imshow(cv2.cvtColor(dst, cv2.COLOR_BGR2RGB))
plt.show()