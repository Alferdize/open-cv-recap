import cv2
print("yes")

img = cv2.imread("resources/lena.png")

cv2.imshow("Output",img)
cv2.waitKey(1000)