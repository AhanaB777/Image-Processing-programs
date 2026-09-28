import cv2 as cv

image = cv.imread("lena.png", 0)

bright = cv.add(image, 50)
dark = cv.subtract(image, 50)
contrast_high = cv.convertScaleAbs(image, alpha=1.5, beta=0)
contrast_low = cv.convertScaleAbs(image, alpha=0.5, beta=0)
negative = 255 - image
_, binary = cv.threshold(image, 128, 255, cv.THRESH_BINARY)

cv.imshow("Original", image)
cv.imshow("Increased Brightness", bright)
cv.imshow("Decreased Brightness", dark)
cv.imshow("Increased Contrast", contrast_high)
cv.imshow("Decreased Contrast", contrast_low)
cv.imshow("Negative Image", negative)
cv.imshow("Binary Threshold", binary)

cv.waitKey(0)
cv.destroyAllWindows()