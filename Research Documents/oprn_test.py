import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

img0 = cv.imread('/home/quixom30/pyton_idle/img/Hrithik.jpeg',0)
#img1 = cv.imread('/home/quixom30/pyton_idle/img/Hrithik.jpeg',1)
#img2 = cv.imread('/home/quixom30/pyton_idle/img/Hrithik.jpeg',-1)

print(type(img0))
#print(img1)
#print(img2)

#cv.namedWindow('Hrithik', cv.WINDOW_NORMAL)
#cv.imshow('Hrithik',img0)
#k = cv.waitKey(0)
#if k == 27:
#    cv.destroyAllWindows()
#else:
#    cv.imwrite('/home/quixom30/pyton_idle/img/Hr.png', img0)
#    cv.destroyAllWindows()

plt.imshow(img0, cmap = 'gray', interpolation = 'bicubic')
plt.xticks([])
plt.yticks([])
plt.show()

print("Hello Nikka...!")
