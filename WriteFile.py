file_object = open("file1.txt","r")
phrase =file_object.read()
file_object.close()
print (phrase)

user = input("Enter the user name")
file_object_new = open("username1.txt","a")
file_object_new.write(user+"\n")
file_object_new.close()

file_object2 = open("username1.txt","r")
userlist= file_object2.read()
print ("The previous user in the file is :")
print (userlist)
