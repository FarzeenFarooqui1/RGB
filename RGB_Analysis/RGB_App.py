import cv2
import os.path
import streamlit as st
import pandas as pd
import numpy
import os     
from natsort import natsorted
import numpy as np
import plotly.express as px
import time
import math


#function for making frames



st.title("Generate RGB values from video")

def reset():
    my_path = os.path.abspath(os.path.dirname(__file__))
    dir_name = os.path.join(my_path, "../Data")
    test = os.listdir(dir_name)
    for item in test:
        if item.endswith(".jpg"):
            (os.remove(os.path.join(dir_name, item)))


my_path = os.path.abspath(os.path.dirname(__file__))
path1 = os.path.join(my_path, "../Data/9convert.com - Color Changing Screen 1 Minute  Mood Led Lights Fast.mp4")

path2 = os.path.join(my_path,"../Data/Forest - 49981.mp4")

path3 = os.path.join(my_path,"../Data/Lake - 64587.mp4")

path4 = os.path.join(my_path,"../Data/Pexels Videos 1918465.mp4")

path5 = os.path.join(my_path,"../Data/Zoom to Fading Supernova in NGC 2525.mp4")

option = st.sidebar.selectbox(
    'Which video?' ,
    ('Select Video','Color Video', 'Forest Video', 'Lake Video','Water Video', 'Supernova Video'))


if option == 'Color Video':
    
    vid = path1

elif option == 'Forest Video':
    
    vid = path2

elif option == 'Lake Video':
    
    vid = path3
elif option == 'Water Video':
    
    vid = path4

elif option == 'Supernova Video':
    
    vid = path5
else:
    
    reset()
    vid = None

st.video(vid)



def frames():
    my_path = os.path.abspath(os.path.dirname(__file__))       
    imagesFolder = os.path.join(my_path, "../Data")
    cap = cv2.VideoCapture(vid)
    frameRate = cap.get(5) #frame rate
    while(cap.isOpened()):
        frameId = cap.get(1) #current frame number
        ret, frame = cap.read()
        if (ret != True):
            break
        if (frameId % math.floor(frameRate) == 0):
            filename = imagesFolder + "/image_" +  str(int(frameId)) + ".jpg"
            cv2.imwrite(filename, frame)
    cap.release()
    

# function for finding RGB
def test():
    my_path = os.path.abspath(os.path.dirname(__file__))
    path_of_images = os.path.join(my_path, "../Data")
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
    

l = [test() for i in range(1)]
def save():

    my_path = os.path.abspath(os.path.dirname(__file__))
    save_path = os.path.join(my_path, "../Output")#path for saving outputed RGB values

    name_of_file = "RGB" #Name of file

    completeName = os.path.join(save_path, name_of_file+".txt") #saves complete name and type of file

    file = open(completeName, "w") #stores file

    str_file = repr(l)
    file.write("a_dictionary = " + str_file + "\n") #writes file
    file.close()

test_data = st.button('Generate frames and extract RGB values of frames')

if test_data:

    frames()

def new_R():
    new_l1=np.delete(l, [1,2], axis=2)
    return (new_l1)

#graphs the Red values
def graph_R():
    fig1 = px.bar(y=RED,title="Red Color Values")
    fig1.update_xaxes(title_text='Time(s)')
    fig1.update_yaxes(title_text='Value R')
    fig1.update_traces(marker_color='rgb(255,0,0)', marker_line_color='rgb(8,48,107)',
                  marker_line_width=1.5, opacity=1)
    st.plotly_chart(fig1)
    my_path = os.path.abspath(os.path.dirname(__file__))
    save_path = os.path.join(my_path, "../Output/fig1.png")
    fig1.write_image(save_path) #saves graph to "Output" folder


# isolates the second column of the list
def new_G():
    new_l2=np.delete(l, [0,2], axis=2)
    return (new_l2)
#graphs the green values
def graph_G():
    fig2 = px.bar(y=(GREEN),title="Green Color Values")
    fig2.update_xaxes(title_text='Time(s)')
    fig2.update_yaxes(title_text='Value G')
    fig2.update_traces(marker_color='rgb(0, 255, 0)', marker_line_color='rgb(8,48,107)',
                  marker_line_width=1.5, opacity=1)
    st.plotly_chart(fig2)
    my_path = os.path.abspath(os.path.dirname(__file__))
    save_path = os.path.join(my_path, "../Output/fig2.png")
    fig2.write_image(save_path) #saves graph to "Output" folder

# isolates the third column of the list
def new_B():
    new_l3=np.delete(l, [0,1], axis=2)
    return (new_l3)

# graphs the blue values
def graph_B():
    fig3 = px.bar(y=(BLUE),title="Blue Color Values")
    fig3.update_xaxes(title_text='Time(s)')
    fig3.update_yaxes(title_text='Value B')
    fig3.update_traces(marker_color='rgb(0, 0, 255)', marker_line_color='rgb(8,48,107)',
                  marker_line_width=1.5, opacity=1)
    st.plotly_chart(fig3)
    my_path = os.path.abspath(os.path.dirname(__file__))
    save_path = os.path.join(my_path, "../Output/fig3.png")
    fig3.write_image(save_path) #saves graph to "Output" folder

analysis = st.sidebar.selectbox('Select Analysis Type',('Generate Graph','Generate Table'))

if analysis == 'Generate Table':
    df = pd.DataFrame(test(), columns=('R','G','B'))
    st.dataframe(df)
    save()
    done = st.button('Finish')

    if done:

        reset()



if analysis == 'Generate Graph':
    
    choice = st.sidebar.selectbox('Select Graph',
        
       ('Red','Green','Blue'))

    try:
        if choice == 'Red':
            new_R()

            RED=new_R().flatten()

            graph_R()
            done = st.button('Delete frames')

            if done:

                reset()


        elif choice == 'Green':

            new_G()

            GREEN=new_G().flatten()

            graph_G()
            done = st.button('Delete frames')

            if done:

                reset()
        elif choice == 'Blue':

            new_B()

            BLUE=new_B().flatten()

            graph_B()
            done = st.button('Delete frames')

            if done:

                reset()


    except numpy.AxisError:
            st.write("First Generate frames!")
   



