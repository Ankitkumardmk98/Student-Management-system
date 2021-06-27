#Student Management System in python
User_Admission = int(input("Enter your Admission no:\n"))
# User_Admission = input("Enter your Admission no:\n")

def user(usr):
    Choose =  int(input("Enter 1 for Inspect, & 2 for Append "))
    if Choose == 1:  #Inspect
        with open(f"{usr}.txt") as file:
            print(file.read())
    elif Choose == 2:  #append
        print('''
              Enter numbers for
              1 for Name
              2 for Roll no
              3 for dob
              ''')
        Detail = int(input("Choose from above option:\n"))
        if Detail == 1:
            nm =  input("Enter your name:\n")
            with open(f"{usr}.txt", "a") as file:
                file.write(f"{nm}\n")
        elif Detail == 2:
            roll =  int(input("Enter your roll number:\n"))
            with open(f"{usr}.txt", "a") as file:
                file.write(f"{roll}\n")
        elif Detail == 3:
            dob =  str(input("Enter your dob number:\n"))
            with open(f"{usr}.txt", "a") as file:
                file.write(f"{dob}\n\n")
        else:
            print("Please Choose right number for appending details")
    
    else:
        print("Please choose right number for inspecting or appending")

user(User_Admission)