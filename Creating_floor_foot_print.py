# -*- coding: utf-8 -*-
"""
Created on Tue Dec 29 06:25:55 2020

@author: us51114
"""
import numpy as np
import cv2 
from Create_lables_for_image import *

def create_text_inside_image(inp_image,text):
    image=inp_image
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
    color = (0., 0, 0) 
    # Line thicknes of 2 px 
    thickness = 1 #2
    #get string size
    img_width=image.shape[1]
    img_height=image.shape[0]
    print(text)
    textSize = cv2.getTextSize(text, font,fontScale, thickness)
    print("intial text size",textSize)
    height=textSize[0][1]
    width=textSize[0][0]
    y_bot=textSize[1]
    total_h=height+y_bot+thickness
    
    diff_w=img_width-width
    if diff_w>0:
        x_pos=int(diff_w/2)
    else:
        x_pos=3
    diff_h=img_height-total_h
    if diff_h>0:
        y_pos=int(diff_h/2)
    else:
        y_pos=3
    org = (x_pos, y_pos)
    image = cv2.putText(image, text, org, font,  
                        fontScale, color, thickness, cv2.LINE_AA)
    return image

def get_blank_set(width_set,height_set):
    thick=1
    image_f=np.zeros([height_set,width_set,3])
    image_f[:]=[255.0,255.0,255.0] #white'
    image_f[:,:thick]=[0,0,0] #black 'left
    image_f[:thick,:]=[0,0,0] #black 'top
    image_f[:,width_set-thick:width_set]=[0,0,0] #black 'right
    image_f[height_set-thick:height_set,:]=[0,0,0] #black 'right
    return image_f


def floor_foot_print(no_r_floor,no_c_floor,title,xlable,ylable,out_img_fn):
    # no_r_floor=5
    # no_c_floor=3
    
    width_set=int(max_img_size/no_r_floor)
    height_set=int(max_img_size/no_c_floor)
    
    total_set_n=no_r_floor*no_c_floor
    
    textSize = cv2.getTextSize("Set " + str(total_set_n), cv2.FONT_HERSHEY_PLAIN,1, 1)
    txt_height=textSize[0][1]
    txt_width=textSize[0][0]
    y_bot=textSize[1]
    thick=1
    total_h=txt_height+y_bot+thick
    
    width_set=max(width_set,txt_width)
    height_set=max(height_set,total_h)
    
    
    image_floor_fp=[]
    set_no=1
    for i in range(no_c_floor):
        row_img=[]
        for j in range(no_r_floor):
            text="Set " + str(set_no)
            image_f=get_blank_set(width_set,height_set)
            # image_f1=image_f[:]
            image_box=create_text_inside_image(image_f,text)
            # cv2.imshow('image',image_f)
            # cv2.waitKey(0)
            # cv2.destroyAllWindows()
            if j==0:
                row_img=image_box
            else:
                row_img=np.concatenate([row_img,image_box],axis=1)
            set_no=set_no+1
        if i==0:
            image_floor_fp=row_img
        else:
            image_floor_fp=np.concatenate([image_floor_fp,row_img])
    
    #below to add title & lables
    title_txt=title #"Rack FootPrint - TopView"
    # x_lable="L=124(mm)"
    # y_lable="W=124(mm)"
    title_img=create_image_for_text(title_txt,0,0)
    xlable_img=create_image_for_text(x_lable,0,0)
    ylable_img=create_image_for_text(y_lable,0,0)
    
    foot_p_w=image_floor_fp.shape[1]
    foot_p_h=image_floor_fp.shape[0]
    title_img_w=title_img.shape[1]
    xlable_img_w=xlable_img.shape[1]
    ylable_img_h=ylable_img.shape[0]
    
    max_w=max(foot_p_w,title_img_w,xlable_img_w)
    max_w=min(max_img_size,max_w)
    max_h=max(foot_p_h,ylable_img_h)
    max_h=min(max_img_size,max_h)
    
    foor_p_resized = cv2.resize(image_floor_fp, (max_w,max_h))
    
    title_img=increase_width_with_white(title_img,max_w)
    print('foot_p_resized:',foot_p_resized.shape)
    print('title_img:',title_img.shape)
    
    final_img=np.concatenate([title_img,foor_p_resized],axis=0)
    xlable_img=increase_width_with_white(xlable_img,max_w)
    final_img=np.concatenate([final_img,xlable_img])
    foot_p_h=final_img.shape[0]
    print('foot_p_h:',foot_p_h)
    ylable_img=increase_width_with_white(ylable_img,foot_p_h)
    print('ylable_img:',ylable_img.shape)
    ylable_img = cv2.rotate(ylable_img, cv2.ROTATE_90_COUNTERCLOCKWISE)
    final_img=np.concatenate([final_img,ylable_img],axis=1)
    cv2.imshow('image',final_img)
    print('final_img:',final_img.shape)
    ka=cv2.imwrite(os.getcwd() + '\\' + out_img_fn,final_img)
    
    img=cv2.imread(os.getcwd() + '\\' + out_img_fn)
    cv2.imshow('image',img)
    
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
    return image_floor_fp

no_r_floor=5
no_c_floor=3
max_img_size=500
title_txt="Floor FootPrint - FrontView"
x_lable="L=124(mm)"
y_lable="W=124(mm)"
out_fn='Floor_topview.jpg'
image_floor_fp=floor_foot_print(no_r_floor,no_c_floor,title_txt,x_lable,y_lable,out_fn)

cv2.imshow('image',image_floor_fp)
cv2.waitKey(0)
cv2.destroyAllWindows()
