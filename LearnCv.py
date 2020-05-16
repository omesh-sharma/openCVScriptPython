

#REFFERENCE  :  https://www.pyimagesearch.com/2018/07/19/opencv-tutorial-a-guide-to-learn-opencv/

## *****************************  BASIC HOW TO READ THE IMAGE IN OPENCV AND FIND THE WIDTH HEIGHT AND DEPTH.******************************8

import imutils
import cv2
# load the input image and show its dimensions, keeping in mind that
# images are represented as a multi-dimensional NumPy array with
# shape no. rows (height) x no. columns (width) x no. channels (depth)
image = cv2.imread("trainOpenCv.jpg")
(h, w, d) = image.shape
print("width={}, height={}, depth={}".format(w, h, d))
# display the image to our screen -- we will need to click the window
# open by OpenCV and press a key on our keyboard to continue execution

#****************************ACCESS individual pixel**********************************************
(B,G,R)= image[100,50]
print("R={},B={},R={}".format(B,G,R))


#cv2.imshow("Image", image)
cv2.waitKey(0)


# ********************** APPLY ROI ********************  region of interest.

ROI = image[60:160,90:420]
#cv2.imshow("ROI",ROI)
cv2.waitKey(0)


# ***************** resize the image ****************
resized = cv2.resize(image,(200,90))
#cv2.imshow("RESIZED",resized)
cv2.waitKey(0)


# ********************* rotating the image ***************************
# let's rotate an image 45 degrees clockwise using OpenCV by first
# computing the image center, then constructing the rotation matrix,
# and then finally applying the affine warp
	
center = (w//2,h//2)
getImageCenter=cv2.getRotationMatrix2D(center,-45,1.0)
rotated=cv2.warpAffine(image,getImageCenter,(w,h))
#cv2.imshow("ROATEDIMAGE",rotated)
cv2.waitKey(0)

#**************  Now we can do the same thing means rotation by just using a imutils.
rotation= imutils.rotate(image,-45)
#cv2.imshow("imutilsRotated",rotation)
cv2.waitKey(0)

### ***************************** Clipping of image *********************
# Once we applied a rotation we are not sure whether rotated image is clipped.

rotated = imutils.rotate_bound(image,45)
#cv2.imshow("clipppedRotation",rotated)
cv2.waitKey(0)

### Smoothing the image .

# apply a Gaussian blur with a 11x11 kernel to the image to smooth it,
# useful when reducing high frequency noise

blurred = cv2.GaussianBlur(image,(11,11),0)
#cv2.imshow("BLURRED",blurred)
cv2.waitKey(0)

###	*************************************  Here We are Applying drawing on image *****************************
# draw a 2px thick red rectangle surrounding the face

drawRectangle= image.copy()
cv2.rectangle(drawRectangle,(100,70),(140,115),(0,0,255),2)
#cv2.imshow("DRAW RECTANGLE",drawRectangle)
cv2.waitKey(0)

## ******************************* LETS DRAW SOME CRICLE OVER THE DEFINED PIXEL********************
# draw a blue 20px (filled in) circle on the image centered at
# x=300,y=150

drawCircle= image.copy();
cv2.circle(drawCircle,(100,150),20,(255,0,0),-1)
#cv2.imshow("CIRCLE OVER PIXEL",drawCircle)
cv2.waitKey(0)

###************************************DRAW A 5 PX THICK LINE   ***********************************************

drawLine=image.copy();
cv2.line(drawLine,(60,10),(150,100),(0,0,255),5)
#cv2.imshow("LINE DRAWING",drawLine)
cv2.waitKey(0)

###### ************************************   PUT THE TExt Over THe Screen*******************************88

# draw green text on the image

insertTextOnImage= image.copy()
cv2.putText(insertTextOnImage,"   OM NAMOH SHIVAY  ",(10,25),cv2.FONT_HERSHEY_SIMPLEX,0.7,(0,255,0),2)
#cv2.imshow("INSERT TEXT ON IMAGE  ",insertTextOnImage)
cv2.waitKey(0)


### Parge the image PAth using argument from command line .
# construct the argument parser and parse the arguments

import argparse
#ap = argparse.ArgumentParser()
##	help="path to input image")
#args = vars(ap.parse_args())
#print(args)


#************************************ CONVERT THE MAGE OT THE GRAYSCALE **********************************
grayScaleColor = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
#cv2.imshow("GRAYSCALEIMAGE",grayScaleColor)
cv2.waitKey(0)

# applying edge detection we can find the outlines of objects in
# images

egdgeOfObject=cv2.Canny(grayScaleColor,30,150)
#cv2.imshow("EDGE DETECTION",egdgeOfObject)
cv2.waitKey(0)

# threshold the image by setting all pixel values less than 225
# to 255 (white; foreground) and all pixel values >= 225 to 255
# (black; background), thereby segmenting the image
#Grabbing all pixels in the gray  image greater than 225 and setting them to 0 (black) which corresponds to the background of the image

thresh = cv2.threshold(grayScaleColor,255,255,cv2.THRESH_BINARY_INV)[1]
#cv2.imshow("GET ThresholdValue",thresh)
cv2.waitKey(0)



#####******************************** DETECTED AND DRAWING CONTOUR.****************************
# find contours (i.e., outlines) of the foreground objects in the
# thresholded image

makeCountable=cv2.findContours(thresh.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
makeCountable=imutils.grab_contours(makeCountable)
resCount=image.copy()

#For Loop Over The Contours
for data in makeCountable:
		#draw each contours over the output image with a 3px thick layer.
		# outline, then display the contours one at the time.
		cv2.drawContours(resCount,[data],-1,(240,0,159),3)
		#cv2.imshow("contours",resCount)
		cv2.waitKey(0)
				
# draw the total number of contours found in purple
text = "I found {} objects!".format(len(makeCountable))
cv2.putText(resCount, text, (10, 25),  cv2.FONT_HERSHEY_SIMPLEX, 0.7,(240, 0, 159), 2)
cv2.imshow("Contours", resCount)
cv2.waitKey(0)