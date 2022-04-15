import os
import cv2 


while True:
    
    print("AVAILABLE PICTURES IN MY FOLDER: \n Just type \n >heart.png \n >star.png")
    image_filename = input("\n Input the filename >>> ")
    print("Image effects list just type the following:  \n >colored \n >grayscale")
    image_flag = input("Image effects >>>")

    if os.path.exists(image_filename) and image_flag == 'colored':
        
        img = cv2.imread(image_filename, 1)
        cv2.imshow(image_filename,img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        print("done")
        break
        
    elif os.path.exists(image_filename) and image_flag == 'grayscale':
         
        img = c.imread(image_filename,0)
        cv2.imshow(image_filename, img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        print("Done!")
        break
    else:
        print("File not found.")
