import cv2

img=cv2.imread("image.jpg")
window_name='imagine RGB'
cv2.namedWindow(window_name, cv2.WINDOW_NORMAL)
cv2.imshow(window_name,img)

image_Gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
window_name='imagine Gray'
cv2.namedWindow(window_name, cv2.WINDOW_NORMAL)
cv2.imshow(window_name,image_Gray)

image_XYZ = cv2.cvtColor(img, cv2.COLOR_RGB2XYZ)
window_name='Imagine XYZ'
cv2.namedWindow(window_name, cv2.WINDOW_NORMAL)
cv2.imshow(window_name,image_XYZ)

image_HSV = cv2.cvtColor(img, cv2.COLOR_RGB2HSV)
window_name='Imagine_HSV'
cv2.namedWindow(window_name, cv2.WINDOW_NORMAL)
cv2.imshow(window_name,image_HSV)

cv2.waitKey(0)
cv2.destroyAllWindows()

