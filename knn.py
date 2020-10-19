# k-nearest Neighbor
# knn은 지도 학습의 가장 간단한 예시인데
# 다양한 레이블의 데이터 중에서, 자신과 가까운 데이터를 찾아 자신의 레이블을 결정하는 방식
import cv2
import numpy as np
from matplotlib import pyplot as plt

train_data = np.random.randint(0,100,(25,2)).astype(np.float32)
print(train_data)
response = np.random.randint(0,2,(25,1)).astype(np.float32)
print(response)
red = train_data[response.ravel()==0]
plt.scatter(red[:,0], red[:,1], 80, 'r', "^")

blue = train_data[response.ravel()==1]
plt.scatter(blue[:,0], blue[:,1],80,'b',"s")

newcomer = np.random.randint(0,100,(1,2)).astype(np.float32)
plt.scatter(newcomer[:,0], newcomer[:,1], 80, 'g', 'o')

knn = cv2.ml.KNearest_create()
knn.train(train_data, cv2.ml.ROW_SAMPLE,response)
ret, results, neighbours, dist = knn.findNearest(newcomer,3)

print('result : ', results)
print('네이버 : ', neighbours)
print('거리 : ', dist)

plt.show()