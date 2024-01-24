import cv2
import matplotlib.pyplot as plt
# Using list comprehension to create a list of x values (0 to 5)
x_values = [x for x in range(6)]

# Specifying the y values for each bar
y_values = [1, 5, 2, 0, 0, 0]

# Creating a bar plot
plt.bar(x_values, y_values)

# Displaying the plot
plt.show()

path = r'C:\Users\T.M.S\OneDrive\Bureau\OPENCV tuto\contt.png'
img=cv2.imread(path)
img1=cv2.flip(img,1)
gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img2=cv2.rotate(img,cv2.ROTATE_90_CLOCKWISE)
img3=-img+255
img4=cv2.convertScaleAbs(img,-1,255)
img5=cv2.equalizeHist(gray_image)
channels = [0]
blue=img[:,:,0]
print(blue)
# Specify the number of bins for each channel
hist_bins = [256]

# Specify the range for each channel
hist_range = [0, 256]

# Calculate the histogram
histogram = cv2.calcHist([img], channels, None, hist_bins, hist_range)
import matplotlib.pyplot as plt

# Example data
categories = ['Category 1', 'Category 2', 'Category 3']
values = [10, 20, 15]

# Creating a bar plot
plt.bar(categories, values)

# Adding labels and title
plt.xlabel('Categories')
plt.ylabel('Values')
plt.title('Bar Plot Example')

# Display the plot
plt.show()

# Print the calculated histogram
plt.plot(histogram)
plt.title('Histogram')
plt.xlabel('Pixel Value')
plt.ylabel('Frequency')
cv2.imshow("flipping image",img5)
cv2.waitKey()
cv2.destroyAllWindows()

#def thresholding(img,threshold,min,max):
 #  N,M=img.shape
  # img1=np.zeros((N,M),dtype=np.uint8)
   #for i in range(N):
  #   for j in range(M):
   #  if img[i,j]>threshold
    #     img1[i,j]=max
     #    else
      #   img1[i,j]=min
