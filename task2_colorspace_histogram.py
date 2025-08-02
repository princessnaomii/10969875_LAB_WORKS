import cv2
import matplotlib.pyplot as plt

# Load the color image
image = cv2.imread('tree.jpg')

# Convert to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imwrite('photo_grayscale.jpg', gray)

# Convert to HSV
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
cv2.imwrite('photo_hsv.jpg', hsv)

# Convert to LAB
lab = cv2.cvtColor(image, cv2.COLOR_BGR2LAB)
cv2.imwrite('photo_lab.jpg', lab)

# Display images
cv2.imshow('Grayscale', gray)
cv2.imshow('HSV', hsv)
cv2.imshow('LAB', lab)

# Plot histogram of the grayscale image
plt.hist(gray.ravel(), bins=256, range=[0, 256])
plt.title('Grayscale Histogram')
plt.xlabel('Pixel Value')
plt.ylabel('Frequency')
plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()
