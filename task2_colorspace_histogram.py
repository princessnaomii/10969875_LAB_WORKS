import cv2
import matplotlib.pyplot as plt

image = cv2.imread('tree.jpg')  
cv2.imshow('Original - BGR', image)

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow('Grayscale', gray)
cv2.imwrite('grayscale.jpg', gray)

hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
cv2.imshow('HSV', hsv)
cv2.imwrite('hsv.jpg', hsv)


lab = cv2.cvtColor(image, cv2.COLOR_BGR2LAB)
cv2.imshow('LAB', lab)
cv2.imwrite('lab.jpg', lab)


plt.figure(figsize=(8, 5))
plt.title('Grayscale Histogram')
plt.xlabel('Pixel value')
plt.ylabel('Frequency')
plt.hist(gray.ravel(), bins=256, range=(0, 256), color='gray')
plt.grid(True)
plt.tight_layout()
plt.savefig('grayscale_histogram.png')
plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()
