import cv2
import os

imgs=[]
while True:
    file = input("Input the filename >>> ")
    
    if file == "QUIT":
        break
    if os.path.exists(file):
        img = cv2.imread(file, 1)
        cv2.imshow("a",img)
        imgs.append(img)
        cv2.waitKey(0)
        c.destroyAllWindows()
        print("done!!!")
        
    else:
        print("File not found.")
