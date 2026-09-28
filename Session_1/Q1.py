import cv2 as cv
import matplotlib.pyplot as plt

# Read image in grayscale
image = cv.imread("lena.png", 0)

# Check if image was loaded
if image is None:
    print("Image not found")
else:
    print("Image loaded successfully")

# Display image using Matplotlib
plt.imshow(image, cmap="gray")
plt.title("Lena - Grayscale")
plt.axis("off")
plt.show()

# Image information
height, width = image.shape

print("Height:", height)
print("Width:", width)
print("Number of pixels:", image.size)
print("Datatype:", image.dtype)

# Minimum and maximum pixel intensity
min_val, max_val, min_loc, max_loc = cv.minMaxLoc(image)

print("Minimum pixel intensity:", min_val)
print("Maximum pixel intensity:", max_val)

# Mean intensity
mean_val = cv.mean(image)[0]
print("Mean intensity:", mean_val)

# Pixel value at (50, 50)
print("Pixel intensity at (50, 50):", image[50, 50])