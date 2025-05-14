# Import OpenCV
import cv2

# Load an image from file
image = cv2.imread('open.jpg')  # Replace with your image path

# Check if image loaded successfully
if image is None:
    print("Error: Could not open or find the image.")
    exit()

# Display the original image
cv2.imshow('Original Image', image)

# Convert the image to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Display the grayscale image
cv2.imshow('Grayscale Image', gray_image)

# Save the grayscale image to file
cv2.imwrite('gray_image_output.jpg', gray_image)

# Wait for a key press and close all windows
cv2.waitKey(0)
cv2.destroyAllWindows()
