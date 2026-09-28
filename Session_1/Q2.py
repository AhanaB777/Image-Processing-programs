import cv2 as cv
import matplotlib.pyplot as plt

# Read image in grayscale
image = cv.imread("lena.png", 0)

# Check if image was loaded
if image is None:
    print("Image not found")
else:
    print("Image loaded successfully")


# 1. Increase Brightness
bright = cv.add(image, 50)


# 2. Decrease Brightness
dark = cv.subtract(image, 50)


# 3. Increase Contrast
contrast_high = cv.convertScaleAbs(image, alpha=1.5, beta=0)


# 4. Decrease Contrast
contrast_low = cv.convertScaleAbs(image, alpha=0.5, beta=0)


# 5. Generate Negative Image
negative = 255 - image


# 6. Binary Thresholding
_, binary = cv.threshold(image, 128, 255, cv.THRESH_BINARY)


# Display all images using Matplotlib
plt.figure(figsize=(12, 8))

plt.subplot(3, 3, 1)
plt.imshow(image, cmap="gray")
plt.title("Original")
plt.axis("off")

plt.subplot(3, 3, 2)
plt.imshow(bright, cmap="gray")
plt.title("Increased Brightness")
plt.axis("off")

plt.subplot(3, 3, 3)
plt.imshow(dark, cmap="gray")
plt.title("Decreased Brightness")
plt.axis("off")

plt.subplot(3, 3, 4)
plt.imshow(contrast_high, cmap="gray")
plt.title("Increased Contrast")
plt.axis("off")

plt.subplot(3, 3, 5)
plt.imshow(contrast_low, cmap="gray")
plt.title("Decreased Contrast")
plt.axis("off")

plt.subplot(3, 3, 6)
plt.imshow(negative, cmap="gray")
plt.title("Negative Image")
plt.axis("off")

plt.subplot(3, 3, 7)
plt.imshow(binary, cmap="gray")
plt.title("Binary Threshold")
plt.axis("off")

plt.tight_layout()
plt.show()