import cv2

# Load the original image

image = cv2.imread('tree.jpg')  
cv2.imshow('Original - BGR', image)
#coverting to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow('Grayscale', gray)

# Save the grayscale image
cv2.imwrite('grayscale.jpg', gray)

cv2.waitKey(0)
cv2.destroyAllWindows()
