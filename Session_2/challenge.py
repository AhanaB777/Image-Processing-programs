import cv2 as cv
import numpy as np

# Read image in grayscale
image = cv.imread("lena.png", 0)

if image is None:
    print("Image not found")
    exit()

print("Image loaded successfully")

# Function for manual nearest-neighbor interpolation
def nearest_neighbor(image, new_height, new_width):

    height, width = image.shape

    # Create output image
    output = np.zeros((new_height, new_width), dtype=image.dtype)

    # Scaling factors
    row_scale = height / new_height
    col_scale = width / new_width

    # Copy nearest pixel
    for i in range(new_height):
        for j in range(new_width):

            old_i = min(int(round(i * row_scale)), height - 1)
            old_j = min(int(round(j * col_scale)), width - 1)

            output[i, j] = image[old_i, old_j]

    return output


# Original image size
height, width = image.shape

print("Original Height:", height)
print("Original Width:", width)


# 2x Zooming
nearest_2x = nearest_neighbor(
    image,
    height * 2,
    width * 2
)


# 4x Zooming
nearest_4x = nearest_neighbor(
    image,
    height * 4,
    width * 4
)


# 1/2 Shrinking
nearest_half = nearest_neighbor(
    image,
    height // 2,
    width // 2
)


# 1/4 Shrinking
nearest_quarter = nearest_neighbor(
    image,
    height // 4,
    width // 4
)


# Display results
cv.imshow("Original", image)
cv.imshow("Nearest Neighbor - 2x", nearest_2x)
cv.imshow("Nearest Neighbor - 4x", nearest_4x)
cv.imshow("Nearest Neighbor - 1/2", nearest_half)
cv.imshow("Nearest Neighbor - 1/4", nearest_quarter)

cv.waitKey(0)
cv.destroyAllWindows()