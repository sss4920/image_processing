import cv2
import numpy as np

img = cv2.imread('digits.png')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#세로로 50줄 가로로 100줄로 사진을 나눕니다.
cells = [np.hsplit(row,100) for row in np.vsplit(gray,50)]
x = np.array(cells)
print(x.shape)

#각 (20 * 20) 크기의 사진을 한 줄(1 * 400)으로 바꿉니다.
train = x[:,:].reshape(-1,400).astype(np.float32) # 모든사진을 일렬로 늘어뜨리겟다
print(train.shape)


# 0이 500개 , 1이 500개, ... 로 총 5000개가 들어가는 (1 * 5000)배열을 만든다

k = np.arange(10) # 0부터 9까지의 그림에 잇는 숫자들을 의미
train_labels = np.repeat(k,500)[:, np.newaxis] # 500번씩 곱함 한숫자당

np.savez("trained.npz", train=train, train_labels=train_labels)
