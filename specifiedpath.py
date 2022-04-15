import cv2
path = 'ILOVEJOY.png'
image = cv2.imread(path,1)
cv2.imshow("IloveJoy", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
print("Done!")
