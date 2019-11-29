import cv2
import numpy as np
import matplotlib as plt

def downsampl(img):
    height, width = img.shape[:2]
    size = (int(width * 0.75), int(height * 0.75))
    img_down=cv2.resize(img, size, interpolation=cv2.INTER_AREA)
    return img_down






def gaoussian_group(img,theta):
    img_w=img.shape[0]
    img_h=img.shape[1]
    img1,img2,img3,img4,img5=np.copy(img)
    imgs = [img1, img2, img3, img4, img5]
    for img in imgs:
        for i in range(img_w):
            for j in range(img_h):
                pass




img=cv2.imread('lena.jpg',cv2.IMREAD_GRAYSCALE)
img1=downsampl(img)
cv2.imshow("mutil_pic", img)
cv2.waitKey(0)