#import matplotlib.pyplot as plt
import numpy as np
import cv2 

#read image
img = cv2.imread("example.jpg")
#image to gray 
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#get image size 
height, width, channels = img.shape
print (height, width, channels)

#get pixel values as tuple 
#bitInfo = image[height, width]

# min and max intensity check for testing
# min = int(img_gray[0,0])
# max = int(img_gray[0,0])

#pixelMap = [height][width]
pixelmap = [[0]*width for i in range(height)]
for i in range(height):
    for j in range(width):
        # if int(pixelmap[i][j]) > max:
        #     max = pixelmap[i][j]
        # if int(pixelmap[i][j]) < min:
        #     min = pixelmap[i][j]
        pixelmap[i][j] = int(img_gray[i,j])

# print("min: ",min)
# print("max: " ,max)

n = int(input("enter matrix dimention: "))

# checking intensity
# for row in pixelmap:
#     print(' '.join([str(elem) for elem in row]))

# loop through the pixel at 3 x 3 at a time and create new pixel map by getting the average of 9 pixels into new pixel map 


#display image
# cv2.imshow("gray", img_gray)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

cv2.imwrite("result.jpg",img)
