import cv2 as cv
import matplotlib.pyplot as plt

image = cv.imread("lena.png", 0)
if image is None:
    print("Image not found")
    exit()
print("Image loaded successfully")

# Nearest-neighbor interpolation
nearest_2x = cv.resize(image, None, fx=2, fy=2, interpolation=cv.INTER_NEAREST)
nearest_4x = cv.resize(image, None, fx=4, fy=4, interpolation=cv.INTER_NEAREST)
nearest_half = cv.resize(image, None, fx=0.5, fy=0.5, interpolation=cv.INTER_NEAREST)
nearest_quarter = cv.resize(image, None, fx=0.25, fy=0.25, interpolation=cv.INTER_NEAREST)

# Bilinear interpolation
bilinear_2x = cv.resize(image, None, fx=2, fy=2, interpolation=cv.INTER_LINEAR)
bilinear_4x = cv.resize(image, None, fx=4, fy=4, interpolation=cv.INTER_LINEAR)
bilinear_half = cv.resize(image, None, fx=0.5, fy=0.5, interpolation=cv.INTER_LINEAR)
bilinear_quarter = cv.resize(image, None, fx=0.25, fy=0.25, interpolation=cv.INTER_LINEAR)

# Bicubic interpolation
bicubic_2x = cv.resize(image, None, fx=2, fy=2, interpolation=cv.INTER_CUBIC)
bicubic_4x = cv.resize(image, None, fx=4, fy=4, interpolation=cv.INTER_CUBIC)
bicubic_half = cv.resize(image, None, fx=0.5, fy=0.5, interpolation=cv.INTER_CUBIC)
bicubic_quarter = cv.resize(image, None, fx=0.25, fy=0.25, interpolation=cv.INTER_CUBIC)

plt.figure(figsize=(12, 4))

plt.subplot(1, 3, 1)
plt.imshow(nearest_2x, cmap="gray")
plt.title("Nearest Neighbor - 2x")
plt.axis("off")

plt.subplot(1, 3, 2)
plt.imshow(bilinear_2x, cmap="gray")
plt.title("Bilinear - 2x")
plt.axis("off")

plt.subplot(1, 3, 3)
plt.imshow(bicubic_2x, cmap="gray")
plt.title("Bicubic - 2x")
plt.axis("off")

plt.tight_layout()
plt.show()