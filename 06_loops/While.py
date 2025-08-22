# while demo 
count = 1
while count <=5:
    print("count", count)
    count += 1

#if you don't know no.of Iterations before hand,use while lopp
# Password validation 
password = "secret"
user_password =""

while user_password != password:
    user_password = input("enter password")
print ("Access Granted")

# Drink water Till Bottle is Empty 
Water_in_bottle = 10
print("Drinking Water")

while water_in_bottle > 0:
    print("Took a sip,remaining sip:", water_in_bottle - 1)
    water_in_bottle -=1