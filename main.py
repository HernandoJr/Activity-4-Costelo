


print("Press [1] To enter specific path"," "," Press[2] To show the specified image")
choice=input("Type here:")
if choice == '2':
   import specifiedpath as fixedpath
   print(fixedpath)
elif choice == '1':   
   import UserPATH as userpath
   print(userpath)
else:
   print("Invalid Input")
   
   
 
