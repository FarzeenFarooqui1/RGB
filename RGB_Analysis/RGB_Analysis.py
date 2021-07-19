#!/usr/bin/env python
# coding: utf-8

# In[1]:


import cv2
import os.path

#function for making frames

def frames():
    cap = cv2.VideoCapture('/Users/farzeent.farooqui/RGB_Analysis/Data/9convert.com - Color Changing Screen 1 Minute  Mood Led Lights Fast.mp4')
    count = 0

    while cap.isOpened():
        ret, frame = cap.read()
    
        if ret:
            save_path = '/Users/farzeent.farooqui/RGB_Analysis/Data'
            name_of_file = 'frame{:d}.jpg'.format(count)
            completeName = os.path.join(save_path, name_of_file)
            cv2.imwrite(completeName, frame)
            count += 5 # i.e. at 5 fps, this advances one second
            cap.set(1, count)
        else:
            cap.release()
            break
frames()


# In[2]:


import cv2  
import numpy
import os     
from natsort import natsorted
# function for finding RGB
def test():
    path_of_images = "/Users/farzeent.farooqui/RGB_Analysis/Data"
    list_of_images = os.listdir(path_of_images)
    result = []
    for image in natsorted(list_of_images):
        myimg = cv2.imread(os.path.join(path_of_images, image))
        if myimg is not None:
            avg_color_per_row = numpy.average(myimg, axis=0)
            avg_color = numpy.average(avg_color_per_row, axis=0)
            avg_rgb = numpy.round(avg_color[::-1]) 
            result.append(avg_rgb)
    return result
test()


# In[3]:


l = [test() for i in range(1)]


# In[6]:


import numpy as np
import plotly.express as px

def new_R():
    new_l1=np.delete(l, [1,2], axis=2)
    return (new_l1)
new_R()

RED=new_R().flatten()

def graph_R():
    df = px.data.tips()
    fig1 = px.bar(y=RED,title="Red Color Values")
    fig1.update_xaxes(title_text='Time(s)')
    fig1.update_yaxes(title_text='Value R')
    fig1.update_traces(marker_color='rgb(255,0,0)', marker_line_color='rgb(8,48,107)',
                  marker_line_width=1.5, opacity=1)
    fig1.show()
    fig1.write_image("Output/fig1.png")
graph_R()

def new_G():
    new_l2=np.delete(l, [0,2], axis=2)
    return (new_l2)
new_G()

GREEN=new_G().flatten()

def graph_G():
    fig2 = px.bar(y=(GREEN),title="Green Color Values")
    fig2.update_xaxes(title_text='Time(s)')
    fig2.update_yaxes(title_text='Value R')
    fig2.update_traces(marker_color='rgb(0, 255, 0)', marker_line_color='rgb(8,48,107)',
                  marker_line_width=1.5, opacity=1)
    fig2.show()
    fig2.write_image("Output/fig2.png")
graph_G()

def new_B():
    new_l3=np.delete(l, [0,1], axis=2)
    return (new_l3)
new_B()

BLUE=new_B().flatten()

def graph_B():
    fig3 = px.bar(y=(BLUE),title="Blue Color Values")
    fig3.update_xaxes(title_text='Time(s)')
    fig3.update_yaxes(title_text='Value R')
    fig3.update_traces(marker_color='rgb(0, 0, 255)', marker_line_color='rgb(8,48,107)',
                  marker_line_width=1.5, opacity=1)
    fig3.show()
    fig3.write_image("Output/fig3.png")
graph_B()


# In[10]:


import os.path

save_path = "/Users/farzeent.farooqui/RGB_Analysis/Output"

name_of_file = "sample.txt"

completeName = os.path.join(save_path, name_of_file+".txt") 

file = open(completeName, "w")

str_file = repr(l)
file.write("a_dictionary = " + str_file + "\n")
file.close()


# In[10]:



# In[ ]:




