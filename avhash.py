from PIL import Image
import numpy as np

def average_hash(fname, size=16):
    img = Image.open(fname)# 이미지 데이터 열기
    # img = img.convert('L')#그레이 스케일로 변환하기
    img = img.resize((size, size), Image.ANTIALIAS) #리사이즈하기
    pixel_data = img.getdata() #픽셀데이터 가져오기
    pixels = np.array(pixel_data) # numpy 배열로 변환하기
    print(pixels)
    pixels = pixels.reshape((size,size)) #2차원 배열로 변환하기
    print(pixels)
    avg = pixels.mean() # 평균구하기
    print(avg)
    diff = 1 * (pixels > avg)
    return diff

def np2hash(ahash):
    bhash = []
    for nl in ahash.tolist():
        s1 = [str(i) for i in nl]
        s2 = "".join(s1)
        i = int(s2,2) #이진수를 정수로 변환하기
        bhash.append("%04x"%i)
    return "".join(bhash)

# Average Hash 출력하기
ahash = average_hash('신발(48).jpg')
print(ahash)
print(np2hash(ahash)) 