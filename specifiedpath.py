
import cv2 as c

class specifiedpath():
   path = 'ILOVEJOY.png'
   image = c.imread(path,1)
   c.imshow("IloveJoy", image)
   c.waitKey(0)
   c.destroyAllWindows()
   print("Done!")
