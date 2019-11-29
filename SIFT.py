import cv2
import numpy as np
import matplotlib as plt
import cv2
import math

def downsampl(img,ratio):
    height, width = img.shape[:2]
    size = (int(width * ratio), int(height * ratio))
    out_img=cv2.resize(img, size, interpolation=cv2.INTER_AREA)
    return out_img



# 参数设置#####

#############


img=cv2.imread('lena.jpg',cv2.IMREAD_GRAYSCALE)
def GaussianPyramid(img,S=5):
    w_H, w_W = img.shape[:2]
    o_num=int(math.log2(min(w_H,w_W)))-3
    imgs=[]
    for i in range(o_num+1):
        imgs.append([])
    sigma_0 = 1.6
    first_img=cv2.resize(img, (int(w_W * 2), int(w_H * 2)), interpolation=cv2.INTER_AREA)
    imgs[0].append(first_img)
    for i in range(0,o_num):
        if i!=0:
            imgs[i].append(downsampl(imgs[i-1][-3],0.5))
        for j in range(0,S+3):
            if j!=0:
                sigma=sigma_0*math.pow(2,(j+1+i)/S)
                img_temp=cv2.GaussianBlur(imgs[i][0],(5,5),sigma)
                imgs[i].append(img_temp)
            # print('高斯',i, j)
            # print(imgs[i][j].shape)
            # cv2.imshow('ss', imgs[i][j])
            # cv2.waitKey(10)
    return imgs

gaussian=GaussianPyramid(img,3)
DOG=[]
for i in range(len(gaussian)):
    DOG.append([])
    for j in range(len(gaussian[i])-1):
        temp_img=gaussian[i][j+1]-gaussian[i][j]
        print('DOG ',i,'  ',j )
        DOG[i].append((temp_img))

img_lab=np.zeros()
for i in range(len(DOG)):
    for j in range(1,len(DOG[i])-1):
        cur_img=DOG[i][j]
        up_img=DOG[i][j+1]
        down_img=DOG[i][j-1]
        img_h,img_w=cur_img.shape[:2]
        for x in range(img_w):
            for y in range(img_h):











