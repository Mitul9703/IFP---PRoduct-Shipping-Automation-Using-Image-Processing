import cv2
from PIL import Image
import matplotlib.pyplot as plt
## reading image
img = cv2.imread('printtest.jpeg',0)
## apply binary thresholding
ret,thresh1 = cv2.threshold(img,170,255,cv2.THRESH_BINARY)
## plot original and binarised image 
titles = ['Original Image', 'Binary Thresholding']
images = [img, thresh1]
for i in range(2):
    plt.figure(figsize=(20,20))
    plt.subplot(2,3,i+1),plt.imshow(images[i],'gray',vmin=0,vmax=255)
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])
        