# Implement Student Management System(LMS)

# we want system info to stored
SYSTEM_INFO = ("LMS Stundent Portal","V10","EDIFY UNIVERSITY")
AMDIN_INFO = ("admin@edify.ai","+91-9876543210","201")

#display System info 
print("="*50)
print(f"WELCOME TO {SYSTEM_INFO[0]}{SYSTEM_INFO[1]}")
print(f"Developed By {SYSTEM_INFO[2]} students")
print("="*50)

# implement Functionalities
#store students info
studnets = {}

while True:
    print("choose an option:")
    print("1 - add student")
    print("2 - Modify student")
    print("3 - Delete Student")
    print("4 - List of all students")
    print("5 - Exit App")

    choice = input("enter your choice (1-5): ")
    if choice == "1":
        print("performing choice 1 Operation")
    elif choice == "2":
        print("performing choice 2 Operation")
    elif choice =="3":
        print("performing choice 3 operation")
    elif choice =="4":
        print("performing choice 4 Operation")
    elif choice == "5":
        print ("performing hoice 5 Operation")
    else : 
        print("Invalid choice select only (1 -5 )")
 
        


