#Student Management System in python
User_Admission = int(input("Enter your Admission no:\n"))
# User_Admission = input("Enter your Admission no:\n")

def user(usr):
    Choose =  int(input("Enter 1 for Inspect, & 2 for Append "))
    if Choose == 1:  #Inspect
        with open(f"{usr}.txt") as file:
            print(file.read())
    elif Choose == 2:  #append
        Detail_nm = input("Enter Your name:\n")
        Detail_roll = int(input("Enter Your roll number:\n"))
        Detail_dob = str(input("Enter Your DOB:\n"))
        
        with open(f"{usr}.txt", "a") as file:
                file.write(f" Name : {Detail_nm}\n Roll no. : {Detail_roll}\n Date of birth : {Detail_dob}\n\n")

    else:
        print("Please choose right number for inspecting or appending")

user(User_Admission)


