import cv2
import numpy as np
src = cv2.imread("sss.jpg", cv2.IMREAD_COLOR)
src_hsv = cv2.cvtColor(src, cv2.COLOR_BGR2HSV)
test = cv2.imread("a.jpg", cv2.IMREAD_COLOR) 
test_hsv = cv2.cvtColor(src, cv2.COLOR_BGR2HSV)
h_s, s_s, v_s = cv2.split(src_hsv)
h_t, s_t, v_t = cv2.split(test_hsv)

# cv2.imshow("h", h_s)
# cv2.imshow("s", s_s)
# cv2.imshow("v", v_s)
# print(h_s)
# h_s = cv2.inRange(h_s,,)
# orange = cv2.bitwise_and(src_hsv, src_hsv, mask=h_s)
# orange = cv2.cvtColor(orange, cv2.COLOR_HSV2BGR)




# img = cv2.imread(src, cv2.IMREAD_COLOR)
hsv_dict = {}
hsv = cv2.cvtColor(src, cv2.COLOR_BGR2HSV)
h,s,v = cv2.split(hsv)

h, cnts = np.unique(h, return_counts=True)
high_freq, high_freq_element = cnts.max(), h[cnts.argmax()]


print(h)
print(cnts)
hsv_dict = dict(zip(h, cnts))

print(high_freq, high_freq_element)

min_freq, min_freq_element = cnts.min(), h[cnts.argmin()]
print(min_freq, min_freq_element)
threshold = 100
s = h.argsort()
print(h[s])

print(h[cnts>threshold])
print(h[cnts>threshold][0])
print(h[cnts>threshold][-1])
h = cv2.inRange(h,13,15)
orange = cv2.bitwise_and(hsv, hsv, mask=h)
orange = cv2.cvtColor(orange, cv2.COLOR_HSV2BGR)
# for hsv_temp in hsv_list:
#     hsv_dict[hsv_temp] = hsv_dict.get(hsv_temp,0)+1
#     keys = sorted(hsv_dict.keys())
# for hsv_temp in keys:
#     print(hsv_temp + ':' + str(hsv_dict[hsv_temp]))





cv2.imshow("orange", orange)
cv2.waitKey(0)
cv2.destroyAllWindows()