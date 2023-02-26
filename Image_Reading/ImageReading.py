import numpy as np
from matplotlib import image
import matplotlib.pyplot as plt
# Download lena.jpg
# Read the image date in a 2D array
# Find the max value of the array
# Find the min value of the array
# Find the average of the image array
# From the image array subtract the average and show the image

def rgb2grey(image):
# Grayscale = 0.299R + 0.587G + 0.114B.   
    grey = image[:,:,0] * 0.299 + image[:,:,1] * 0.587 + image[:,:,2] * 0.114
    return grey

img = image.imread("swan.jpg")
print(type(img))
print(img.shape)
grey = rgb2grey(img)
print(grey.shape)

plt.imshow(grey, cmap='gray')
plt.show()
print("max value of grey image is {}".format(np.max(grey)))
print("min value of grey image is {}".format(np.min(grey)))
print("avg value of grey image is {}".format(np.average(grey)))

# gray_average = grey - np.average(grey)
gray_1_0 = np.zeros(grey.shape)
for i in range(grey.shape[0]):
    for j in range(grey.shape[1]):
        if grey[i, j] > 100:
            gray_1_0[i, j] = 0
        else:
            gray_1_0[i, j] = grey[i, j]
        
            
        
    
plt.imshow(gray_1_0, cmap ='gray')
plt.show()