import cv2
import os.path
import streamlit as st
import pandas as pd
import numpy
import os     
from natsort import natsorted
import numpy as np
import plotly.express as px
import os.path



#function for making frames


st.title("Generate RGB values from video")


sidebar_selection = st.sidebar.radio(
    'Navigation:',
    ['Get RGB Values', 'Generate Graphs', 'Delete Frames'],
)



my_path = os.path.abspath(os.path.dirname(__file__))
path1 = os.path.join(my_path, "../Data/9convert.com - Color Changing Screen 1 Minute  Mood Led Lights Fast.mp4")

path2 = os.path.join(my_path,"../Data/Forest - 49981.mp4")

path3 = os.path.join(my_path,"../Data/Lake - 64587.mp4")

path4 = os.path.join(my_path,"../Data/Pexels Videos 1918465.mp4")

path5 = os.path.join(my_path,"../Data/Zoom to Fading Supernova in NGC 2525.mp4")

option = st.selectbox(
    'Which video?',
    (path1, path2, path3,path4,path5))

st.write('You selected:', option)

st.sidebar.write("Video preview:")
st.sidebar.video(option)

cap = cv2.VideoCapture(option)


def frames():

    count = 0

    while cap.isOpened():
        ret, frame = cap.read()
    
        if ret:
            my_path = os.path.abspath(os.path.dirname(__file__))
            option = os.path.join(my_path, "../Data")
            name_of_file = 'frame{:d}.jpg'.format(count)
            completeName = os.path.join(option, name_of_file)
            cv2.imwrite(completeName, frame)
            count += 5 # i.e. at 5 fps, this advances one second
            cap.set(1, count)
        else:
            cap.release()
            break

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


if sidebar_selection == 'Get RGB Values':
    test_data = st.button('Generate frames and get RGB values of frames')
    if test_data:
        frames()
        st.dataframe(test())
        save()

def new_R():
    new_l1=np.delete(l, [1,2], axis=2)
    return (new_l1)

#graphs the Red values
def graph_R():
    df = px.data.tips()
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
    fig2.update_yaxes(title_text='Value R')
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
    fig3.update_yaxes(title_text='Value R')
    fig3.update_traces(marker_color='rgb(0, 0, 255)', marker_line_color='rgb(8,48,107)',
                  marker_line_width=1.5, opacity=1)
    st.plotly_chart(fig3)
    my_path = os.path.abspath(os.path.dirname(__file__))
    save_path = os.path.join(my_path, "../Output/fig3.png")
    fig3.write_image(save_path) #saves graph to "Output" folder

if sidebar_selection == 'Generate Graphs':
    create_graphs = st.button('Generate graphs')

    option = st.selectbox(
        'Which graph?',
        ('Red','Green','Blue'))


    if option == 'Red':
        new_R()

        RED=new_R().flatten()

        graph_R()
    if option == 'Green':

        new_G()

        GREEN=new_G().flatten()

        graph_G()
    if option == 'Blue':

        new_B()

        BLUE=new_B().flatten()

        graph_B()


if sidebar_selection == 'Delete Frames':

    st.header("Delete Frames stored in Data folder")
    delete_frames = st.button('Delete frames')

    if delete_frames:
        my_path = os.path.abspath(os.path.dirname(__file__))
        dir_name = os.path.join(my_path, "../Data")
        test = os.listdir(dir_name)

        for item in test:
            if item.endswith(".jpg"):
                os.remove(os.path.join(dir_name, item))





