import cv2
import numpy as np

qimg = cv2.imread('신발(50).jpg',cv2.IMREAD_COLOR)
qimg = cv2.cvtColor(qimg, cv2.COLOR_BGR2GRAY)
timg = cv2.imread('신발(51).jpg',cv2.IMREAD_COLOR)
timg = cv2.cvtColor(timg, cv2.COLOR_BGR2GRAY)
rimg = cv2.imread('sss.jpg',cv2.IMREAD_COLOR)
rimg = cv2.cvtColor(rimg, cv2.COLOR_BGR2GRAY)
res1, res2 = None, None
# sift
sift = cv2.xfeatures2d.SIFT_create()

# keypoints & descriptors
kp1, des1 = sift.detectAndCompute(qimg,None)
kp2, des2 = sift.detectAndCompute(timg,None)
kp3, des3 = sift.detectAndCompute(rimg,None)

#flann params
FLANN_INDEX_KDTREE = 0
index_params = dict(algorithm=FLANN_INDEX_KDTREE, trees=5)
search_params = dict(checks=50) # 아니면 비워둔 딕셔너리 그대로

flann =cv2.FlannMatcher(index_params, search_params)

matches1 = flann.knnMatch(des1, des2, k=2)
matches2 = flann.knnMatch(des1, des3, k=2)

# 좋은 매칭만 그려야함, 그래서 마스크를 만들어야함
# 1순위 매칭, 2순위 매칭]을 담는다
matchesMask = [[0,0] for i in range(len(matches))] # len(matches) 만큼 [0,0] 생성

# ratio test
for i,(m,n) in enumerate(matches1):
    if m.distance < 0.7*n.distance:
        matchesMask[i] = [1,0]

draw_params = dict(matchColor = (0,255,0),
                singlePointColor = (255,0,0),
                matchesMask = matchesMask,
                flags = 0)

res1 = cv2.drawMatchesKnn(qimg,kp1,timg,kp2,matches1,res1,**draw_params)

cv2.imshow('FLANN', res1)
cv2.waitKey(0)
cv2.destroyAllWindows()