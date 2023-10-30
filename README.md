# search-and-rescue
## About
Search and Rescue model to detect features within an input image. Feature detection includes differentiating between burnt and unburnt grass
and finding areas of interests such as edges, corners and simple shapes. These features are then
classified into various categories based on their shape, colour or other inherent features. These
concepts are widely used in military and civilian UAV missions to gather information about areas
out of human reach, such as disaster-stricken or mountainous areas.


## Compatibility
Python - version 3.8 

## Dataset
Images with clear differentiation between burnt and unburnt grass.
Houses represented by red BGR(0,0,255) or blue BGR(255,0,0) coloured triangles.

## Instructions to Run
-pip install numpy
-pip install opencv-python

Enter the path to the folder where the dataset is saved in 'line 28'
Example: "C:\\Users\\XYZ\\*.png"

## Result
Successfully return images with clear differentiation between burnt and unburnt grass
Classified houses in either of the areas and calculated priority order according to a set priority number


