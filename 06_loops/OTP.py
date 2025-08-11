import random 
#assume the correct OTP is already stored in a variable
otp = random.randint(1000,9999)
print(otp)

#while loop
#after 3 inccorect attempt,display
#maximum attempts done, try after 24 hours
count = 3

while count>0:

    #condition 
    #if otp entered in not 4 digit 
    #otp must be 4 digital number only 
    user_otp = int(input("enter OTP:"))

    if len(str(user_otp))!=4:#type: ignore
        print("OTP must be 4 digital number only")
    #If the OTP is correct,display:
    #correct OTP - success
    if OTP == user_otp #type: ignore
        print("correct OTP")
        break
    count = count -1

    #last msg to display 

else :
    print("Max attempt Done, try after 24 hours")
