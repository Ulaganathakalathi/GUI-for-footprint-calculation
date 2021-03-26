# -*- coding: utf-8 -*-
"""
Created on Mon Dec 28 10:25:17 2020

@author: us51114
#to create lable for the image
"""
import cv2 
import numpy as np
import os
# path 
# path = r'C:\Users\Rajnish\Desktop\geeksforgeeks\geeks.png'
    
# Reading an image in default mode 
# image = cv2.imread(path) 


# image=[]
# cv2.imshow('image',image)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
def create_image_for_text(text,req_width,rotate_deg):
    # font 
    # font=cv2.FONT_HERSHEY_SIMPLEX 
    font = cv2.FONT_HERSHEY_PLAIN 
    # font= cv2.FONT_HERSHEY_DUPLEX
    # font=cv2.FONT_HERSHEY_COMPLEX
    # font=cv2.FONT_HERSHEY_TRIPLEX
    # font=cv2.FONT_HERSHEY_COMPLEX_SMALL
    # font=cv2.FONT_HERSHEY_SCRIPT_SIMPLEX
    # font=cv2.FONT_HERSHEY_SCRIPT_COMPLEX
    # fontScale 
    fontScale = 1 #1
    # Blue color in BGR 
    color = (255, 0, 0) 
    # Line thicknes of 2 px 
    thickness = 1 #2
    #get string size
    textSize = cv2.getTextSize(text, font,fontScale, thickness)
    
    height=textSize[0][1]
    width=textSize[0][0]
    y_bot=textSize[1]
    total_h=height+y_bot+thickness
    h_add=8
    if req_width>width:
        diff_w=req_width-width
        org = (int(diff_w/2), int(height/2+y_bot+thickness+h_add/2))
        image=np.zeros([total_h+h_add,req_width,3])
    else:
        org = (0, int(height/2+y_bot+thickness+h_add/2)) # org
        image=np.zeros([total_h+h_add,width,3])
    
    # print(y_bot)
    image[:]=255
    # print(textSize)
    print(textSize)
    # Using cv2.putText() method 
    # bas_l=cv2.LINE_AA
    # print(bas_l)
    image = cv2.putText(image, text, org, font,  
                        fontScale, color, thickness, cv2.LINE_AA) 
    print(image.shape)
    # print("act_width & act_height",req_width,req_hight)
    if (req_width<width) and (req_width!=0):
        ratio_w=req_width/width
        req_hight=ratio_w*(total_h+h_add)
        print("req_width & req_height",req_width,req_hight)
        image=cv2.resize(image, (int(req_width),int(req_hight)))#, interpolation = cv2.INTER_AREA)
    if rotate_deg!=0:
        print(cv2.ROTATE_90_COUNTERCLOCKWISE)
        image = cv2.rotate(image, cv2.ROTATE_90_COUNTERCLOCKWISE)
    return image

def increase_width_with_white(image,req_width):
    act_width=image.shape[1]
    if req_width>act_width:
        diff_width=req_width-act_width
        diff_w_half=int(diff_width/2);diff_add=0
        if diff_w_half*2!=diff_width:
            diff_add=diff_width-diff_w_half*2
        act_height=image.shape[0]
        image_f=np.zeros([act_height,diff_w_half,3])
        print(image[0,0])
        image_f[:]=image[0,0]
        image_b=np.zeros([act_height,diff_w_half+diff_add,3])
        # print(image[0,0])
        image_b[:]=image[0,0]
        image=np.concatenate([image_f,image,image_b],axis=1)
    return image


# Displaying the image 
text = "Hi Image(mm)"
req_width=400
image=create_image_for_text(text,req_width,0)
cv2.imshow('image', image)  
cv2.waitKey(0)
cv2.destroyAllWindows()
ka=cv2.imwrite(os.getcwd() + '\\FONT_HERSHEY_SCRIPT_COMPLEX.jpg',image)
print('start_w',image.shape[1])
img_inc_w=increase_width_with_white(image,image.shape[1])
print('end_w',img_inc_w.shape[1])
cv2.imshow('image', img_inc_w)  
cv2.waitKey(0)
cv2.destroyAllWindows()