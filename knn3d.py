# k-nearest Neighbor
# knn은 지도 학습의 가장 간단한 예시인데
# 다양한 레이블의 데이터 중에서, 자신과 가까운 데이터를 찾아 자신의 레이블을 결정하는 방식
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
import pandas as pd
    # img = img.convert('L')#그레이 스케일로 변환하기
    # img = img.resize((16, 16), Image.ANTIALIAS) #리사이즈하기

def rgb_plot(fname):
    img = Image.open(fname)# 이미지 데이터 열기
    img = img.convert('RGB')
    pixel_data = img.getdata() #픽셀데이터 가져오기
    pixels = np.array(pixel_data) # numpy 배열로 변환하기
    n = pixels.size//3 #이게 점의 개수란 말이지
    # cluster = np.zeros((n,1), dtype=np.int64)
    # np.append(pixels, cluster, axis=1)
    
    
    xmin, xmax, ymin, ymax, zmin, zmax = 0, 255, 0, 255, 0, 255
    cmin, cmax = 0, 2
    xs = pixels[:,0]
    ys = pixels[:,1]
    zs = pixels[:,2]
    # cluster = pixels[:,3]
    color = np.array([(cmax - cmin) * np.random.random_sample() + cmin for i in range(n)])

    fig = plt.figure(figsize=(6, 6))
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(xs, ys, zs, c=color, marker='o', s=15, cmap='Greens')
    ax.set_xlabel('red', fontsize=14)
    ax.set_zlabel('green', fontsize=14)
    ax.set_ylabel('blue', fontsize=14)

    plt.show()

    df = pd.DataFrame(pixels)
    df.to_csv('rgb-csv/shoes{}.csv'.format(fname),index=['red','green','blue'])
category = ['shoes','t-shirts']
image_name = '신발(47).jpg'
rgb_plot(image_name)
