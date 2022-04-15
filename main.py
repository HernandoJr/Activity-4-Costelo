while True:
   print("=================================================")
   print("Press [1] To enter specific path"," "," Press[2] To show the specified image")
   choice=input("Type here:")

   if choice == '2':
      import specifiedpath 
      break
   elif choice == '1':   
      import UserPATH 
      break
   else:
      print("Invalid Input\n")
   
   
 
