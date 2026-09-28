import cv2 as cv
import numpy as np

# Read image
image = cv.imread("lena.png")

if image is None:
    print("Image not found")
    exit()

print("Image loaded successfully")

# 1. Translation
# Move image 100 pixels right and 50 pixels down
M = np.float32([[1, 0, 100],
                [0, 1, 50]])

translated = cv.warpAffine(image, M, (image.shape[1], image.shape[0]))

# 2. Scaling
# Scale image by 1.5 times
scaled = cv.resize(image, None, fx=1.5, fy=1.5)

# 3. Rotation
# Rotate image by 45 degrees
height, width = image.shape[:2]
center = (width // 2, height // 2)

M = cv.getRotationMatrix2D(center, 45, 1)
rotated = cv.warpAffine(image, M, (width, height))

# 4. Horizontal Reflection
horizontal = cv.flip(image, 1)

# 5. Vertical Reflection
vertical = cv.flip(image, 0)

# Display images
cv.imshow("Original", image)
cv.imshow("Translation", translated)
cv.imshow("Scaling", scaled)
cv.imshow("Rotation", rotated)
cv.imshow("Horizontal Reflection", horizontal)
cv.imshow("Vertical Reflection", vertical)

cv.waitKey(0)
cv.destroyAllWindows()