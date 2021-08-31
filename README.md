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
The purpose of this project is to record a video from the user's webcam and then output the RGB spectrum of each frame and display them in a graph. 


### Built With

* [Streamlit](https://streamlit.io)
* [Python](https://www.python.org/downloads/)





<!-- USAGE EXAMPLES -->
## Usage

1. There is a start button that can be used to record video from the users webcam or there are also multiple pre uploaded videos saved into the "Data" folder. The user can either choose to analyze a pre uploaded video or analyze their own recorded video. The "Frames" function is then run which divides the video into frames at a rate of 1 frames per second.
2. The "Test" function will then find all the created frames in the "Data" folder but only look at the ones that are image files. It will then print out the RGB values of every frame in an organized list of Numpy arrays.
3. The list is then converted into a variable that can be used throughout the program. 
4. The functions "new_R", "new_G", "new_B" will then take the indiviual columns of the numpy array and store them as variables.
5. The 2D arrays are then all flattened into more workable 1D arrays.
6. The "Graph_R",Graph_G", Graph_B" functions will then return a bar graph of the RGB values of every image. 
7. The delete frames button can be used to delete existing frames so that analysis can be done on a new video




<!-- CONTACT -->
## Contact

Farzeen Farooqui - ffarooq5@uwo.ca

Project Link: [https://github.com/FarzeenFarooqui1/RGB_Analysis.git](https://github.com/FarzeenFarooqui1/RGB_Analysis.git)





