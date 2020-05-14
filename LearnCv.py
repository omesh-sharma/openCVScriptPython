

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

# ********************** APPLY ROI ********************  region of interest.

ROI = image[60:160,90:420]
#cv2.imshow("ROI",ROI)

# ***************** resize the image ****************
resized = cv2.resize(image,(200,90))
#cv2.imshow("RESIZED",resized)

# ********************* rotating the image ***************************
# let's rotate an image 45 degrees clockwise using OpenCV by first
# computing the image center, then constructing the rotation matrix,
# and then finally applying the affine warp
	
center = (w//2,h//2)
getImageCenter=cv2.getRotationMatrix2D(center,-45,1.0)
rotated=cv2.warpAffine(image,getImageCenter,(w,h))
#cv2.imshow("ROATEDIMAGE",rotated)

#**************  Now we can do the same thing means rotation by just using a imutils.
rotation= imutils.rotate(image,-45)
#cv2.imshow("imutilsRotated",rotation)

### ***************************** Clipping of image *********************
# Once we applied a rotation we are not sure whether rotated image is clipped.

rotated = imutils.rotate_bound(image,45)
#cv2.imshow("clipppedRotation",rotated)


### Smoothing the image .

# apply a Gaussian blur with a 11x11 kernel to the image to smooth it,
# useful when reducing high frequency noise

blurred = cv2.GaussianBlur(image,(11,11),0)
#cv2.imshow("BLURRED",blurred)


###	*************************************  Here We are Applying drawing on image *****************************
# draw a 2px thick red rectangle surrounding the face

drawRectangle= image.copy()
cv2.rectangle(drawRectangle,(100,70),(140,115),(0,0,255),2)
#cv2.imshow("DRAW RECTANGLE",drawRectangle)


## ******************************* LETS DRAW SOME CRICLE OVER THE DEFINED PIXEL********************
# draw a blue 20px (filled in) circle on the image centered at
# x=300,y=150

drawCircle= image.copy();
cv2.circle(drawCircle,(100,150),20,(255,0,0),-1)
#cv2.imshow("CIRCLE OVER PIXEL",drawCircle)

###************************************DRAW A 5 PX THICK LINE   ***********************************************

drawLine=image.copy();
cv2.line(drawLine,(60,10),(150,100),(0,0,255),5)
#cv2.imshow("LINE DRAWING",drawLine)

###### ************************************   PUT THE TExt Over THe Screen*******************************88

# draw green text on the image

insertTextOnImage= image.copy()
cv2.putText(insertTextOnImage,"   OM NAMOH SHIVAY  ",(10,25),cv2.FONT_HERSHEY_SIMPLEX,0.7,(0,255,0),2)
cv2.imshow("INSERT TEXT ON IMAGE  ",insertTextOnImage)
cv2.waitKey(0)