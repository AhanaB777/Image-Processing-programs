import numpy as np
import cv2 as cv

image=cv.imread("lena.png", 0)

# 1. Increase brightness using NumPy
bright_np = np.clip(image.astype(np.int16) + 50, 0, 255).astype(np.uint8)

# 2. Generate negative image using NumPy
negative_np = 255 - image

# 3. Binary thresholding using NumPy
binary_np = np.where(image >= 128, 255, 0).astype(np.uint8)


# Display the results using OpenCV
cv.imshow("Brightness using NumPy", bright_np)
cv.imshow("Negative using NumPy", negative_np)
cv.imshow("Binary Threshold using NumPy", binary_np)

cv.waitKey(0)
cv.destroyAllWindows()