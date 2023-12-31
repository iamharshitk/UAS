
#~~~~~~~  SEARCH AND RESCUE ~~~~~~~

#Importing modules
import cv2 as cv
import numpy as np


#Importing glob library to process multiple images
import glob


#BGR of red colour 
red_bgr=np.array([0,0,255])

#BGR of blue colour 
blue_bgr=np.array([255,0,0])


#Initialising lists to store data
Hb_and_Hg=[]
Pb_and_Pg=[]
priority_order=[]
image_by_ratio=[]


#Enter the path of the folder where the images are stored
#Example: "C:\\Users\\XYZ\\*.png"
img_path="Path"



#Using a for loop to process images
for file in glob.glob(img_path):
 
 #Reading the current image
 img=cv.imread(file)
 
 #Making 2 copies of the original image
 output_img=img.copy()
 copy2=img.copy()

 #Converting the image from BGR to HSV 
 hsv_img=cv.cvtColor(img,cv.COLOR_BGR2HSV)

 #Making lists to store the locations of the detected houses
 red_burnt=[]
 blue_burnt=[]

 red_unburnt=[]
 blue_unburnt=[]





 #Defining a function to mask the burnt area 
 def burnt_grass():


    #Selecting a colour range in HSV for classification of burnt grass using a numpy array
    lower_limit=np.array([0,20,0])
    upper_limit=np.array([30,255,250])


    #Converting the image into binary form for easier differentiation b/w burnt and unburnt grass
    bin_img = cv.inRange(hsv_img, lower_limit, upper_limit)


    #Finding contours in the binary image
    contours, _ = cv.findContours(bin_img, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)


    #Masking the burnt area, making changes in the output image
    cv.drawContours(output_img, contours, -1, (0, 255, 255), -1)


    #Executing functions for identification of houses in the unmasked area
    triangles(output_img, red_unburnt, red_bgr)
    triangles(output_img, blue_unburnt, blue_bgr)


    #Executing a function to recognise and mask the unburnt area using the second copy of the original image
    unburnt_grass()





 #Function to mask the unburnt area 
 def unburnt_grass():

    #Converting the image into binary form for easier differentiation b/w burnt and unburnt grass
    lower_limit=np.array([30,30,30])
    upper_limit=np.array([90,255,250])

    bin_img = cv.inRange(hsv_img, lower_limit, upper_limit)

    #Finding the contours in the binary image
    contours, _ = cv.findContours(bin_img, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)

    
    #Masking the unburnt area
    cv.drawContours(copy2, contours, -1, (230, 230, 50), -1)
    cv.drawContours(output_img, contours, -1, (230, 230, 50), -1)

    #Executing functions to recognise houses in the unmasked area
    triangles(copy2, red_burnt, red_bgr)
    triangles(copy2, blue_burnt, blue_bgr)




 #Function to recognise houses
 def triangles(xyz_img, xyz_list, colour_bgr):
    
    #Converting to binary
    bin_img=cv.inRange(xyz_img, colour_bgr, colour_bgr)

    #Finding contours
    contours, _= cv.findContours(bin_img, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)

    #Looping over the contours to identify triangles
    for i in contours:
        accuracy=0.25*cv.arcLength(i, True)
        vertices=cv.approxPolyDP(i, accuracy, True)

        #Setting conditions for the detection of a triangle with an area greater than 500 pixels
        if len(vertices)==3 and cv.contourArea(vertices)>500:
            xyz_list.append(vertices)




 #Function to draw the houses on the output image
 def draw_triangle():
    for i in red_burnt:
        cv.drawContours(output_img, [i], 0, (0, 0 ,255), -1)
    for i in red_unburnt:
        cv.drawContours(output_img, [i], 0, (0, 0 ,255), -1)
    for i in blue_burnt:
        cv.drawContours(output_img, [i], 0, (255, 0 ,0), -1)
    for i in blue_unburnt:
        cv.drawContours(output_img, [i], 0, (255, 0 ,0), -1)

 


 #Executing the functions
 burnt_grass()
 draw_triangle()
 

 #Calculating the output
 burnt_unburnt=[len(red_burnt)+len(blue_burnt),len(red_unburnt)+len(blue_unburnt)]

 burntprior_unburntprior=[len(red_burnt)+2*len(blue_burnt),len(red_unburnt)+2*len(blue_unburnt)]

 rescue_ratio=burnt_unburnt[0]/burnt_unburnt[1]


 #Storing the output
 Hb_and_Hg.append(burnt_unburnt)
 Pb_and_Pg.append(burntprior_unburntprior)
 priority_order.append(rescue_ratio)
 image_by_ratio.append([file,rescue_ratio])

 #Printing the location of the current image
 print(file)

 
 #Opening the output image
 cv.imshow(file, output_img)
 cv.waitKey(0)
 cv.destroyAllWindows()


#Printing the output
print("Number of houses on the burnt grass and the number of houses on the green:\n")
print(Hb_and_Hg,"\n")
print("The total priority of houses on the burnt grass and the total priority of houses on the green grass:\n")
print(Pb_and_Pg,"\n")
print("Rescue ratio of priority:\n")
print(priority_order,"\n")


#~~~~~~~~~~~~~~~~END OF CODE~~~~~~~~~~~~~~~~

   












    








