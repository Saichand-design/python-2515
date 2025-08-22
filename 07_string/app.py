Username = input("enter username")

#check if given username has more than 4 characters
if len(Username) >= 4:
    print("actual Given",Username)
    print("Fromated Output", Username.lower())
    if Username.lower().find("@") != -1:
        print("vaild Email")
    else:
        print("invaild Email")
    
else:
    print ("username should be atleast 4 or above chars")

pan = input("Enter PAN:")
formatted_pan = pan.upper()
print("Fromatted PAN", formatted_pan)
print("hello")