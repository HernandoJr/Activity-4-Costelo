import os
import cv2 


while True:
    print("=================================================================")
    print("AVAILABLE PICTURES IN MY FOLDER(Type the filename with extension!):\n>heart.png \n>star.png")
    image_filename = input("\n Input the filename >>> ")
    print("Image effects:\n","Press[0] Grayscale\n Press[1] Colored")
    image_flag = input("Image effects flag: >>>")

    if os.path.exists(image_filename) and image_flag == '1':
        
        img = cv2.imread(image_filename, 1)
        cv2.imshow(image_filename,img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        print("done")
        break
        
    elif os.path.exists(image_filename) and image_flag == '0':
         
        img = cv2.imread(image_filename,0)
        cv2.imshow(image_filename, img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        print("Done!")
        break
    else:
        
        print("\n--File not found or Invalid Input--")
