file_object = open("file1.txt","w")
#phrase = "The first content"
file_object.write("Jawahar Santhiya Navajith")
file_object.close()
file_object1 = open("file1.txt","r")
content = file_object1.read()
print (content)
file_object1.close()


user = input("Enter the user name"+"\n")
file_object_new = open("username1.txt","a")
file_object_new.write(user+"\n")
file_object_new.close()

file_object2 = open("username1.txt","r")
userlist= file_object2.read()
print ("The previous user in the file is :")
print (userlist)
