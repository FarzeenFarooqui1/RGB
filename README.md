<!-- PROJECT LOGO -->


  <h3 align="center">RGB-Analysis</h3>

  <p align="center">
    <br />
    <br />
    <br />
  
  </p>
</p>



<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary>Table of Contents</summary>
  
1.<a href="#about-the-project">About The Project</a>
   <ul>
     <li><a href="#built-with">Built With</a></li>
   </ul>
   
2.<a href="#usage">Usage</a>
    
3.<a href="#contact">Contact</a>
    </li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project
The purpose of this project was to create an app that can record video from a smartphone’s camera and output the RGB values of each frame at a rate of one frame per second. These RGB values can be displayed either in a table or as bar graphs. This app can be used to test the water quality of a sample by finding the RGB values of any particulates in the water.

### Built With

* [Streamlit](https://streamlit.io)
* [Python](https://www.python.org/downloads/)





<!-- USAGE EXAMPLES -->
## Usage
The interface is shown below:
![image info](/Pictures/Screen Shot 2021-09-05 at 9.39.21 PM.png)

1. There is a start button that can be used to record video from the users webcam or there are also multiple pre uploaded videos saved into the App. The user can either choose to analyze a pre uploaded video or analyze their own recorded video. The app divides the video into frames at a rate of 1 frames per second.
2. When the user clicks the button labeled "Generate Frames and Extract RGB Values of Frames" app will then find all the created frames in the "Data" folder but only look at the ones that are image files. It will then print out the RGB values of every frame either as a table or graphs.
3. The user can choose from the sidebar which whether they want to view the RGB values as either a table or a graph. If graph is selected then the user can select from the sidebar if they want to see the red, green or blue graph.
4. The "Delete Frames" button at the bottom of the app can reset the app by deleting the previous video's frames.



<!-- CONTACT -->
## Contact

Farzeen Farooqui - ffarooq5@uwo.ca

Project Link: [https://github.com/FarzeenFarooqui1/RGB_Analysis.git](https://github.com/FarzeenFarooqui1/RGB_Analysis.git)

Streamlit App Link: [https://share.streamlit.io/farzeenfarooqui1/rgb_analysis/main/RGB_Analysis/RGB_App.py](https://share.streamlit.io/farzeenfarooqui1/rgb_analysis/main/RGB_Analysis/RGB_App.py)






