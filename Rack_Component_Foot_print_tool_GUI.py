# -*- coding: utf-8 -*-
"""
Created on Tue Dec 29 18:15:07 2020

@author: us51114
"""

import tkinter as tk
import random
import os
from PIL import Image, ImageTk
global root
import win32com.client

def create_entry(master,title_width,title_txt,lable_txt,frame_w,lab_width,com_height,entry_width,pad_h,start_y,start_x,no_colum,entry_create=1):
    com_width=lab_width
    if title_txt!="":
        title_label=tk.Label(master,text=title_txt,bg='white')
        space_dif=frame_w-title_width
        title_label.place(x=int(space_dif/2),y=start_y,width=title_width,height=com_height)
        
        #below is for lables for inputs
        # lable_txt=['No of Rows', 'No of Columns','No of Layers','Spacing between two parts (mm) G1','Spacing between two layers (mm) G2','Distance from Vertical Post (mm) G3/G4']
        
        start_y=start_y+com_height+pad_h
    listOfEntries=[]
    # print('lable_txt-len',len(lable_txt),'& no_colum:',no_colum)
    for i in range(0,len(lable_txt),no_colum):
        # print('i=',i)
        start_x_loc=start_x
        if lable_txt[i]!='':
            part_l=tk.Label(master,text=lable_txt[i],bg='white')
            part_l.place(x=start_x,y=start_y,width=com_width,height=com_height)
            start_x_loc=start_x_loc+com_width+5
        if entry_create==1:
            entry_1=tk.Entry(master) #, width = com_width)
            entry_1.place(x=start_x_loc,y=start_y,width = entry_width,height = com_height)
            listOfEntries.append(entry_1)
            start_x_loc=start_x_loc+entry_width+5
        # start_x_2=start_x
        for j in range(1,no_colum):
            # print('j=',j)
            if i+j<len(lable_txt):
                # start_x_2=start_x_2+com_width+5+entry_width+5
                if lable_txt[i+j]!='':
                    part_l=tk.Label(master,text=lable_txt[i+j],bg='white')
                    part_l.place(x=start_x_loc,y=start_y,width=com_width,height=com_height)
                    start_x_loc=start_x_loc+com_width+5
                if entry_create==1:
                    entry_1=tk.Entry(master) #, width = com_width)
                    entry_1.place(x=start_x_loc,y=start_y,width = entry_width,height = com_height)
                    listOfEntries.append(entry_1)
                    start_x_loc=start_x_loc+entry_width+5
        start_y=start_y+com_height+pad_h
    return listOfEntries,start_y

global input_data_val
input_data_val=list(range(19))  #kalathi: command this at the end

def create_input_frame(root):
        #create frame
    global list_input_entry #listOfEntries_part,listOfEntries_partmatrix,listOfEntries_rackspace,listOfEntries_floor_fp,listOfEntries_space_utlz
    global frame_input
    frame_w=500;frame_h=500
    com_height=25;com_width=150;entry_width=70
    pad_h=5;start_x=20;start_y=pad_h
    list_input_entry=[]
    
    frame_input=tk.Frame(root,bg='blue')
    frame_input.place(x=200,y=10,width=frame_w,height=frame_w)
    all_frames.append(frame_input)
    
    #below for header title
    # title_label=tk.Label(frame,text='Enter Input Information',bg='white')
    # title_label.place(x=0,y=start_y,width=frame_w,height=com_height)
    
    # #part input for rack foot print
    # start_y=start_y+com_height+pad_h
    
    title_txt='Input for Rack-Footprint Calculation'
    title_width=400;no_colum=2
    lable_txt=['Part Number', 'Part Weight (kg)','Part Length (mm)','Part Width (mm)','Part Height (mm)']
    listOfEntries_part,start_y =create_entry(frame_input,title_width,title_txt,lable_txt,frame_w,com_width,com_height,entry_width,pad_h,start_y,start_x,no_colum)
    # list_input_entry.append(listOfEntries_part[i] for i in range(len(listOfEntries_part)))
    list_input_entry.append(listOfEntries_part)
    
    #part matrix input
    title_txt='Input for Rack Part Matrix'
    title_width=300;no_colum=2
    lable_txt=['No of Rows', 'No of Columns','No of Layers','Rack Empty Weight']
    listOfEntries_partmatrix,start_y =create_entry(frame_input,title_width,title_txt,lable_txt,frame_w,com_width,com_height,entry_width,pad_h,start_y,start_x,no_colum)
    # list_input_entry.append(listOfEntries_partmatrix[i] for i in range(len(listOfEntries_partmatrix)))
    list_input_entry.append(listOfEntries_partmatrix)
    
    #rack spacing input
    title_txt=''
    title_width=300;no_colum=1
    lable_txt=['Spacing between two parts (mm) G1','Spacing between two layers (mm) G2','Distance from Vertical Post (mm) G3/G4']
    listOfEntries_rackspace,start_y =create_entry(frame_input,title_width,title_txt,lable_txt,frame_w,250,com_height,entry_width,pad_h,start_y,start_x,no_colum)
    # list_input_entry.append(listOfEntries_rackspace[i] for i in range(len(listOfEntries_rackspace)))
    list_input_entry.append(listOfEntries_rackspace)
    
    #Floor Footprint input
    title_txt='Input for Floor-Footprint Calculation'
    title_width=400;no_colum=2
    lable_txt=['Total No of Racks','Total No of Stacks','No of Rows','No of Columns', 'Spacing-X (mm)','Spacing-Y (mm)']
    listOfEntries_floor_fp,start_y =create_entry(frame_input,title_width,title_txt,lable_txt,frame_w,com_width,com_height,entry_width,pad_h,start_y,start_x,no_colum)
    # list_input_entry.append(listOfEntries_floor_fp[i] for i in range(len(listOfEntries_floor_fp)))
    list_input_entry.append(listOfEntries_floor_fp)
    
    #Space utilization input
    title_txt='Input for Space Utilizaion Calculation'
    title_width=400;no_colum=2
    lable_txt=['Container ISO code']
    listOfEntries_space_utlz,start_y =create_entry(frame_input,title_width,title_txt,lable_txt,frame_w,com_width,com_height,entry_width,pad_h,start_y,start_x,no_colum)
    # list_input_entry.append(listOfEntries_space_utlz[i] for i in range(len(listOfEntries_space_utlz)))
    list_input_entry.append(listOfEntries_space_utlz)
    if len(input_data_val)>0:
        indx_i=0
        for i in range(len(list_input_entry)):
            for j in range(len(list_input_entry[i])):
                dat_val=input_data_val[indx_i]
                list_input_entry[i][j].insert(0,dat_val)
                indx_i=indx_i+1
                # if dat_val!=0:
                #     list_input_entry[i][j].insert(0,str(dat_val)) #set(str(dat_val))
                # indx_i=indx_i+1
                # if dat_ent=="":
                #     input_data_val.append(0.0)
                # else:
                #     input_data_val.append(float(dat_ent))
        
    # print(list_input_entry)


def get_input_data():
    input_data_val.clear()
    # ind_i=1
    for i in range(len(list_input_entry)):
        for j in range(len(list_input_entry[i])):
            dat_ent=list_input_entry[i][j].get()
            input_data_val.append(dat_ent)
    # print(input_data_val)

global calc_out_data
calc_out_data=[]

def output_calculation():
    #
    global input_data_val
    calc_out_data.clear()
    input_data_val1=input_data_val[:]
    for i in range(1,len(input_data_val1)-1):
        if input_data_val1[i]=='':
            input_data_val1[i]=0.0
        else:
            input_data_val1[i]=float(input_data_val1[i])
            
    part_num=input_data_val[0]
    part_weig=input_data_val1[1]
    part_len=input_data_val1[2]
    part_width=input_data_val1[3]
    part_heigt=input_data_val1[4]
    part_matrix_no_r=input_data_val1[5]
    part_matrix_no_c=input_data_val1[6]
    part_matrix_no_lay=input_data_val1[7]
    Rack_empty_weight=input_data_val1[8]
    G1=input_data_val1[9]
    G2=input_data_val1[10]
    G3=input_data_val1[11]
    
    #Rack foot print Calculaion
    Gross_rack_weight=(part_weig)*(part_matrix_no_r*part_matrix_no_c*part_matrix_no_lay)+Rack_empty_weight
    Stock_thick=4.7752 #kalathi: need to extracted from data base
    Stock_L1=63.5 #kalathi: need to extracted from data base
    Stock_L2=63.5 #kalathi: need to extracted from data base
    Rack_fp_L=part_len*part_matrix_no_r+G1*(part_matrix_no_r-1)+2*G3+2*Stock_L1
    Rack_fp_W=part_width*part_matrix_no_c+G1*(part_matrix_no_c-1)+2*G3+2*Stock_L1
    Rack_fp_H=part_heigt*part_matrix_no_lay+G2*(part_matrix_no_lay-1)+165.1+63.5
    rack_vol=Rack_fp_L*Rack_fp_W*Rack_fp_H
    
    calc_out_data.append(Rack_fp_L)
    calc_out_data.append(Rack_fp_W)
    calc_out_data.append(Rack_fp_H)
    calc_out_data.append(Stock_L1)
    calc_out_data.append(Stock_L2)
    calc_out_data.append(Stock_thick)
    
    
    floor_no_rack=input_data_val1[12]
    floor_no_stack=input_data_val1[13]
    floor_no_r=input_data_val1[14]
    floor_no_c=input_data_val1[15]
    floor_spacing_x=input_data_val1[16]
    floor_spacing_y=input_data_val1[17]
    
    
    #Floor Footprint Calculation
    floor_space_x=floor_no_r*Rack_fp_L+(floor_no_r-1)*floor_spacing_x
    floor_space_y=floor_no_c*Rack_fp_W+(floor_no_c-1)*floor_spacing_y
    floor_space_require=floor_space_x*floor_space_y/1000000 #in Sq.meter
    stack_height=Rack_fp_H*floor_no_stack
    
    calc_out_data.append(floor_space_x)
    calc_out_data.append(floor_space_y)
    calc_out_data.append(floor_space_require)
    calc_out_data.append(stack_height)
    
    #Space Utilization Calculation
    container_code=input_data_val[18]
    container_L=5895.0 #kalathi: need to extract from data base
    container_W=2350.0 #kalathi: need to extract from data base
    container_H=2392.0 #kalathi: need to extract from data base
    container_capacity=20000.0 #kalathi: need to extract from data base
    
    container_vol=container_L*container_W*container_H
    
    LenWise_no_row=container_L//Rack_fp_L
    WidWise_no_row=container_W//Rack_fp_L
    LenWise_no_col=container_W//Rack_fp_W
    WidWise_no_col=container_L//Rack_fp_W
    LenWise_no_stack=container_H//Rack_fp_H
    WidWise_no_stack=container_H//Rack_fp_H
    
    LenWise_no_rack_dim=LenWise_no_row*LenWise_no_col*LenWise_no_stack
    WidWise_no_rack_dim=WidWise_no_row*WidWise_no_col*WidWise_no_stack
    
    no_rack_as_weig=container_capacity//Gross_rack_weight
    
    LenWise_no_rack=min(LenWise_no_rack_dim,no_rack_as_weig)
    WidWise_no_rack=min(WidWise_no_rack_dim,no_rack_as_weig)
    
    LenWise_s_Utlz=(LenWise_no_rack*rack_vol/container_vol)*100
    LenWise_weig_Utlz=(LenWise_no_rack*Gross_rack_weight/container_capacity)*100
    
    WidWise_s_Utlz=(WidWise_no_rack*rack_vol/container_vol)*100
    WidWise_weig_Utlz=(WidWise_no_rack*Gross_rack_weight/container_capacity)*100
    
    calc_out_data.append(LenWise_no_rack)
    calc_out_data.append(LenWise_s_Utlz)
    calc_out_data.append(LenWise_weig_Utlz)
    calc_out_data.append(WidWise_no_rack)
    calc_out_data.append(WidWise_s_Utlz)
    calc_out_data.append(stack_height)
    

def create_output_frame(root):
    #%% calculation output frame
        #create frame
    # global listOfEntries_part,listOfEntries_partmatrix,listOfEntries_rackspace,listOfEntries_floor_fp,listOfEntries_space_utlz
    global frame_out
    global list_output_entry
    global listOfEntries_RFS #'Length,width,height,L1,L2,Thickness'
    global listOfEntries_FFP #Floor Space-X, Floor Space-Y, Floor space required(m^2), Stacking height
    global listOfEntries_SUtlz #Len_wise: No of racks, Space Utlz, Weight Utlz,width_wise: No of racks, Space Utlz, Weight Utlz
    list_output_entry=[]
    
    
    frame_w=500;frame_h=500
    com_height=25;com_width=150;entry_width=70
    pad_h=5;start_x=20;start_y=pad_h
    
    frame_out=tk.Frame(root,bg='blue')
    frame_out.place(x=200,y=10,width=frame_w,height=frame_w)
    all_frames.append(frame_out)
    
    title_x=2
    #below for header title
    title_label=tk.Label(frame_out,text='Output from Rack-Footprint Calculation',bg='white')
    title_label.place(x=title_x,y=start_y,width=frame_w-title_x*2,height=com_height)
    
    #rack foot print calculation output
    start_y=start_y+com_height+pad_h
    
    title_txt='Rack-Footprint Size'
    title_width=300;no_colum=3
    lable_txt=['Length (mm)', 'Width (mm)','Height (mm)']
    listOfEntries_RFS,start_y =create_entry(frame_out,title_width,title_txt,lable_txt,frame_w,80,com_height,entry_width,pad_h,start_y,start_x,no_colum)
    list_output_entry.append(listOfEntries_RFS)
    
    title_txt='Stock Size'
    title_width=300;no_colum=3
    lable_txt=['L1 (mm)', 'L2(mm)']
    com_width_loc=70
    listOfEntries_RSS,start_y =create_entry(frame_out,title_width,title_txt,lable_txt,frame_w,com_width_loc,com_height,entry_width,pad_h,start_y,start_x,no_colum)
    list_output_entry.append(listOfEntries_RSS)
    
    start_x_loc=start_x+(com_width_loc+5+entry_width+5)*2
    start_y=start_y-(com_height+pad_h)
    lable_txt=['Thickness (mm)']
    listOfEntries_th,start_y =create_entry(frame_out,title_width,'',lable_txt,frame_w,90,com_height,entry_width,pad_h,start_y,start_x_loc,no_colum)
    list_output_entry.append(listOfEntries_th)
    
    # listOfEntries_RSS.append(listOfEntries_th[0])
    # listOfEntries_RFS.append(listOfEntries_RSS)
    #'Length,width,height,L1,L2,Thickness'
    
    #below for header title for floor foot print
    title_label=tk.Label(frame_out,text='Output from Floor-Footprint Calculation',bg='white')
    title_label.place(x=title_x,y=start_y,width=frame_w-title_x*2,height=com_height)
    
    #floor foot print calculation output
    start_y=start_y+com_height+pad_h
    
    title_txt=''
    title_width=400;no_colum=2
    lable_txt=['Floor Space-X (mm)', 'Floor Space-Y (mm)']
    listOfEntries_FFP,start_y =create_entry(frame_out,title_width,title_txt,lable_txt,frame_w,com_width,com_height,entry_width,pad_h,start_y,start_x,no_colum)
    list_output_entry.append(listOfEntries_FFP)
    
    title_txt=''
    title_width=400;no_colum=10
    lable_txt=['Floor space required (m^2)','Stacking height (mm)']
    com_width_loc=com_width
    listOfEntries_FFP1,start_y =create_entry(frame_out,title_width,title_txt,lable_txt,frame_w,com_width_loc,com_height,entry_width,pad_h,start_y,start_x,no_colum)
    list_output_entry.append(listOfEntries_FFP1)
    
    # listOfEntries_FFP.append(listOfEntries_FFP1)
    #Floor Space-X, Floor Space-Y, Floor space required(m^2), Stacking height
    
    #below for header title for space Utilization
    title_label=tk.Label(frame_out,text='Output from Space Utilization Calculation',bg='white')
    title_label.place(x=title_x,y=start_y,width=frame_w-title_x*2,height=com_height)
    
    #space Utilization calculation output
    start_y=start_y+com_height+pad_h
    
    title_txt=''
    title_width=400;no_colum=3
    lable_txt=['No of Rack', 'Space Utilisation (%)', 'Weight Utilisation (%)']
    com_width_loc=80
    start_x_loc=start_x+com_width_loc+5
    listOfEntries_SUtlz,start_y =create_entry(frame_out,title_width,title_txt,lable_txt,frame_w,120,com_height,entry_width,pad_h,start_y,start_x_loc,no_colum,entry_create=0)
    
    
    
    title_txt=''
    title_width=400;no_colum=4
    lable_txt=['Length wise','','']
    listOfEntries_SUtlz,start_y =create_entry(frame_out,title_width,title_txt,lable_txt,frame_w,com_width_loc,com_height,120,pad_h,start_y,start_x,no_colum)
    list_output_entry.append(listOfEntries_SUtlz)
    
    title_txt=''
    title_width=400;no_colum=4
    lable_txt=['width wise','','']
    listOfEntries_SUtlz1,start_y =create_entry(frame_out,title_width,title_txt,lable_txt,frame_w,com_width_loc,com_height,120,pad_h,start_y,start_x,no_colum)
    list_output_entry.append(listOfEntries_SUtlz1)
    
    # listOfEntries_SUtlz.append(listOfEntries_FFP1)
    #Len_wise: No of racks, Space Utlz, Weight Utlz,width_wise: No of racks, Space Utlz, Weight Utlz
    
    if len(calc_out_data)>0:
        indx_i=0
        for i in range(len(list_output_entry)):
            for j in range(len(list_output_entry[i])):
                dat_val=calc_out_data[indx_i]
                if indx_i==10 or indx_i==13:
                    dat_val=int(dat_val)
                else:
                    dat_val=round(dat_val,2)
                # if type(dat_val)==float():
                #     print(dat_val)
                #     # dat_val=round(dat_val,2)
                list_output_entry[i][j].insert(0,dat_val)
                indx_i=indx_i+1
                
def create_output_label_for_img(root,input_img):
    #%% footprint image view frame
        #create frame
    # global listOfEntries_part,listOfEntries_partmatrix,listOfEntries_rackspace,listOfEntries_floor_fp,listOfEntries_space_utlz
    global frame_out_label_img
    global out_img_lab #display image
    
    frame_w=500;frame_h=500
    com_height=25;com_width=150;entry_width=70
    pad_h=5;start_x=20;start_y=pad_h
    
    frame_out_label_img=tk.Frame(root,bg='red')
    frame_out_label_img.place(x=200,y=10,width=frame_w,height=frame_w)
    all_frames.append(frame_out_label_img)
    out_img_lab=tk.Label(frame_out_label_img,image=input_img)
    out_img_lab.place(x=0,y=0,width=frame_w,height=frame_h)
    out_img_lab.image = input_img

    
def output_option_frame(root): #this is frame to show the bottens for output view option
    global frame_out_option,out_opt_buttons
    frame_w=500;frame_h=50
    # com_height=25;com_width=150;entry_width=70
    pad_h=5;start_x=20;start_y=pad_h
    frame_out_option=tk.Frame(root,bg='red')
    frame_out_option.place(x=200,y=10+500+10,width=frame_w,height=frame_h)
    
    button_txt = ['Calculated Values','Rack footprint-TopView','Rack footprint-FrontView','Floor footprint-TopView']
    start_x_b=5;start_y_b=5;b_width=119;b_height=40
    out_opt_buttons=create_buttons(frame_out_option,button_txt,start_x_b,start_y_b,b_width,b_height)
    for i in range(len(out_opt_buttons)):
        out_opt_buttons[i].configure(wraplength=110)
    out_opt_buttons[0].configure(command=show_calculated_output_vales)
    out_opt_buttons[1].configure(command=Rack_footprint_topview_but)
    out_opt_buttons[2].configure(command=Rack_footprint_frontview_but)
    out_opt_buttons[3].configure(command=show_Floor_FP_Topview)
    all_frames.append(frame_out_option)

global auto_view
auto_view=True
global rack_fp_topview_img,rack_fp_frontview_img,rack_fp_topview_user_img,rack_fp_frontview_user_img
global floor_fp_topview_img
rack_fp_topview_img='Rack_topview.jpg'
rack_fp_frontview_img='Rack_frontview.jpg'
rack_fp_topview_user_img='Rack_user_topview.jpg'
rack_fp_frontview_user_img='Rack_user_frontview.jpg'
floor_fp_topview_img='Floor_topview.jpg'

def Rack_footprint_topview_but():
    global rack_top_view,auto_view
    rack_top_view=True
    if auto_view:
        ka=show_Rack_image(rack_fp_topview_img)
    else:
        ka=show_Rack_image(rack_fp_topview_user_img)
    ka=rack_option_frame(root)

def Rack_footprint_frontview_but():
    global rack_top_view,auto_view
    rack_top_view=False
    if auto_view:
        ka=show_Rack_image(rack_fp_frontview_img)
    else:
        ka=show_Rack_image(rack_fp_frontview_user_img)
    ka=rack_option_frame(root)
    
def show_Rack_image(img_fname): #to show the Rack Footprint top view
    try: 
        frame_out.place_forget()
    except: 
        ka=""
    # print("entered: Rack footprint-TopView")
    img_fn=os.getcwd() + '\\' + img_fname #'topview.jpg' #cD:\kalathi\My_collection\Python\Automation_to_Creo\topview.jpg
    image1 = Image.open(img_fn)
    image1 = image1.resize((500, 500), Image.ANTIALIAS)
    image1 = ImageTk.PhotoImage(image1)
    ka=create_output_label_for_img(root,image1)
    # ka=rack_option_frame(root)

# def show_Rack_FP_frontview(img_fname='frontview.jpg'): #to show the Rack Footprint fri=ont view
#     try:
#         frame_out.place_forget()
#     except:
#         ka=1
#     try:
#         frame_out_label_img.place_forget()
#     except:
#         ka=1
#     # print("Rack footprint-FrontView'")
#     # frame_to_hide=[frame_out,frame_out_label_img]
#     # try: frame_out.place_forget(); except: ka="";
#     # try: frame_out_label_img.place_forget(); except: ka="";
#     img_fn=os.getcwd() + '\\' + img_fname #'frontview.jpg' #cD:\kalathi\My_collection\Python\Automation_to_Creo\topview.jpg
#     image1 = Image.open(img_fn)
#     image1 = image1.resize((500, 500), Image.ANTIALIAS)
#     image1 = ImageTk.PhotoImage(image1)
#     ka=create_output_label_for_img(root,image1)
#     rack_top_view=False
#     ka=rack_option_frame(root)

def show_Floor_FP_Topview(): #to show the Floor Footprint fri=ont view
    try:
        frame_out.place_forget()
    except:
        ka=1
    try:
        frame_out_label_img.place_forget()
    except:
        ka=1
    try:
        frame_rack_option.place_forget()
        # print('forgoted:frame_rack_option')
    except:
        ka=1
    # frame_to_hide=[frame_out,frame_out_label_img]
    # try: frame_out.place_forget(); except: ka="";
    # try: frame_out_label_img.place_forget(); except: ka="";
    img_fn=os.getcwd() + '\\' + floor_fp_topview_img #cD:\kalathi\My_collection\Python\Automation_to_Creo\topview.jpg
    image1 = Image.open(img_fn)
    image1 = image1.resize((500, 500), Image.ANTIALIAS)
    image1 = ImageTk.PhotoImage(image1)
    ka=create_output_label_for_img(root,image1)
    
    # ka=rack_option_frame(root)

def show_calculated_output_vales(): #to show the calculated output values
    try:
        frame_out.place_forget()
    except:
        ka=1
    try:
        frame_out_label_img.place_forget()
    except:
        ka=1
    try:
        frame_rack_option.place_forget()
    except:
        ka=1
    ka=create_output_frame(root)

global rack_top_view #variable to identify Rack footprint is active at Topview or front view
rack_top_view=True

def rack_option_frame(root): #this frame as button change the view of image to Auto view or User view
    global frame_rack_option,rack_opt_buttons
    # print('entered for rack_option_frame')
    try:
        frame_rack_option.place_forget()
    except:
        ka=1
    frame_w=160;frame_h=100
    # com_height=25;com_width=150;entry_width=70
    pad_h=5;start_x=20;start_y=pad_h
    frame_rack_option=tk.Frame(root,bg='yellow')
    frame_rack_option.place(x=40,y=10+500/2-frame_h/2,width=frame_w,height=frame_h)
    button_txt = ['Auto View','User View','Get User View from Creo']
    start_x_b=5;start_y_b=5;b_width=150;b_height=25
    out_opt_buttons=create_buttons(frame_rack_option,button_txt,start_x_b,start_y_b,b_width,b_height,horizontal=0)
    out_opt_buttons[0].configure(command=Auto_View_button)
    out_opt_buttons[1].configure(command=User_View_button)
    out_opt_buttons[2].configure(command=get_user_view_from_creo_but)
    # for i in range(len(out_opt_buttons)):
    #     out_opt_buttons[i].configure(wraplength=110)
    all_frames.append(frame_rack_option)

def get_user_view_from_creo_but():
    ka=run_macro_to_get_userview_image()
    ka=User_View_button()
    
def Auto_View_button():
    # global rack_top_view
    # rack_top_view_loc=rack_top_view
    global auto_view
    auto_view=True
    # print("rack_top_view:",rack_top_view)
    if rack_top_view:
        ka=show_Rack_image(rack_fp_topview_img)
    else:
        ka=show_Rack_image(rack_fp_frontview_img)
    # rack_top_view=rack_top_view_loc

global user_image_creo_extrated
user_image_creo_extrated=False

# print('hi')
def User_View_button():
    # global rack_top_view
    # rack_top_view_loc=rack_top_view
    # print("rack_top_view:",rack_top_view)
    global auto_view,user_image_creo_extrated
    # print('enter user_image_creo_extrated:',user_image_creo_extrated)
    if not user_image_creo_extrated:
        ka=run_macro_to_get_userview_image()
        # user_image_creo_extrated=True
    auto_view=False
    if user_image_creo_extrated:
        if rack_top_view:
            ka=show_Rack_image(rack_fp_topview_user_img)
        else:
            ka=show_Rack_image(rack_fp_frontview_user_img)
    else:
        if rack_top_view:
            ka=show_Rack_image(rack_fp_topview_img)
        else:
            ka=show_Rack_image(rack_fp_frontview_img)
    # print('exist user_image_creo_extrated:',user_image_creo_extrated)
    # rack_top_view=rack_top_view_loc
        
def create_buttons(master,button_txt,start_x_b,start_y_b,b_width,b_height,horizontal=1):
    # languages = ['Input','Calculate','Exit'] #,'Java','Tcl/Tk']
    # labels = range(5)
    # start_x_b=20;start_y_b=30;b_width=120;b_height=25
    gap_s=5
    if horizontal==1:
        x_mult=1;y_mult=0
    else:
        x_mult=0;y_mult=1
    buttons=[]
    for i in range(len(button_txt)):
        ct = [random.randrange(256) for x in range(3)]
        brightness = int(round(0.299*ct[0] + 0.587*ct[1] + 0.114*ct[2]))
        ct_hex = "%02x%02x%02x" % tuple(ct)
        bg_colour = '#' + "".join(ct_hex)
        l = tk.Button(master, 
                     text=button_txt[i], 
                     fg='White' if brightness < 120 else 'Black', 
                     bg=bg_colour)
        l.place(x = start_x_b+i*(b_width+gap_s)*x_mult, y = start_y_b+i*(b_height+gap_s)*y_mult, width=b_width, height=b_height)
        buttons.append(l)
    return buttons


def show_input_frame():
    ka=clear_all_frames()
    ka=create_input_frame(root)
    # tk.messagebox.showinfo( "Hello Python", "Hello World")

global creo_image_extracted, prev_part, prev_part_L,prev_part_W,prev_part_H
creo_image_extracted=False

def show_output_frame():
    global creo_image_extracted, prev_part, prev_part_L,prev_part_W,prev_part_H
    ka=get_input_data()
    
    #below calculate output values
    ka=output_calculation()
    
    # print('completed get_input_data')
    ka=create_output_frame(root)
    
    #below to collect the image from creo
    check_rs=check_creo_image_extract_or_not()
    # print('check_rs',check_rs)
    if check_rs:
        ka=run_macro_to_get_image()
        global input_data_val
        prev_part=input_data_val[0]
        prev_part_L=input_data_val[2]
        prev_part_W=input_data_val[3]
        prev_part_H=input_data_val[4]
        creo_image_extracted=True
    
    # print('create_output_frame')
    ka=output_option_frame(root)
    # print('create_output_frame')

def check_creo_image_extract_or_not():
    global creo_image_extracted
    if not creo_image_extracted:
        return True
    global prev_part, prev_part_L,prev_part_W,prev_part_H
    global input_data_val
    if prev_part!=input_data_val[0] or prev_part_L!=input_data_val[2] or prev_part_W!=input_data_val[3] or prev_part_H!=input_data_val[4]:
        return True
    else:
        return False

def hide_frame(input_list):
    # for i in range(len(input_list)):
    try:
        input_list.place_forget()
    except:
        kk=1

def run_macro_to_get_image():
    tk.messagebox.showinfo( "Hello Python", "Auto image created")
    # xl=win32com.client.DispatchEx("Excel.Application")
    # xl.Workbooks.Open(os.getcwd() + "\\Macro_run.xlsm") #D:\kalathi\My_collection\Python\Automation_to_Creo\
    # global input_data_val
    # part_no=input_data_val[0]
    # part_len=input_data_val[2]
    # part_width=input_data_val[3]
    # part_heigt=input_data_val[4]
    # xl.workbooks("Macro_run.xlsm").activesheet.cells(2,1).value=part_len
    # xl.workbooks("Macro_run.xlsm").activesheet.cells(2,2).value=part_width
    # xl.workbooks("Macro_run.xlsm").activesheet.cells(2,3).value=part_heigt
    # xl.Visible=True
    # xl.application.run('Macro_run.xlsm!kalathi')
    # xl.workbooks("Macro_run.xlsm").save
    # xl.Application.Quit()

def run_macro_to_get_userview_image():
    global user_image_creo_extrated
    msg_info='Before using get user view, user need to create Topview and Frontview in the Creo.'
    user_opt=tk.messagebox.askyesnocancel ('Yes or No or Cancel action Box',msg_info)
    if user_opt:
        tk.messagebox.showinfo( "Hello Python", "User image created")
        user_image_creo_extrated=True
        # xl=win32com.client.DispatchEx("Excel.Application")
        # xl.Workbooks.Open(os.getcwd() + "\\Macro_run.xlsm") #D:\kalathi\My_collection\Python\Automation_to_Creo\
        # global input_data_val
        # part_len=input_data_val[2]
        # part_width=input_data_val[3]
        # part_heigt=input_data_val[4]
        # xl.workbooks("Macro_run.xlsm").activesheet.cells(2,1).value=part_len
        # xl.workbooks("Macro_run.xlsm").activesheet.cells(2,2).value=part_width
        # xl.workbooks("Macro_run.xlsm").activesheet.cells(2,3).value=part_heigt
        # xl.Visible=True
        # xl.application.run('Macro_run.xlsm!kalathi')
        # xl.workbooks("Macro_run.xlsm").save
        # xl.Application.Quit()
        # user_image_creo_extrated=True
    else:
        tk.messagebox.showinfo( "Hello Python", "User image not created")
        user_image_creo_extrated=False

def clear_all_frames():
    # all_frames=[frame_input,frame_out,frame_out_option,frame_rack_option]
    
    for i in range(len(all_frames)):
        try:
            all_frames[i].place_forget()
        except:
            kk=1
    all_frames.clear()
    
global all_frames
all_frames=[]



root = tk.Tk()

root.title("Rack Pre-Concepting Tool")


# width x height + x_offset + y_offset:
root.geometry("800x580+30+30") 

#create main buttons
button_txt = ['Input','Calculate','Exit']
start_x_b=20;start_y_b=30;b_width=120;b_height=25
master_buttons=create_buttons(root,button_txt,start_x_b,start_y_b,b_width,b_height,horizontal=0)

    

master_buttons[0].configure(command=show_input_frame) #Input
master_buttons[1].configure(command=show_output_frame) #Calculate
master_buttons[2].configure(command=clear_all_frames) #Exit



root.mainloop()