def User():
    User_Input = int(input("Enter 1 to Inspect or 2 to Update: "))
    if User_Input == 1: #Inspect
        try:
            Admission_No = int(input("Enter Addmision no: "))
            with open(f"{Admission_No}.txt", "r") as file:
                print(file.read())
        except Exception as Error:
            print(f" No Student Found with this Addmisiion no \n {Error}")
    
    elif User_Input == 2:  #Update
        Admission_No = int(input("Enter Addmision no: "))
        with open(f"{Admission_No}.txt", "a") as file:
            User_Name = input("Enter Name: ")
            User_Roll = int(input("Enter Roll: "))
            User_DOB = input("Enter DOB: ")
            
            file.write(f'''
Name : {User_Name} 
Roll : {User_Roll} 
DOB : {User_DOB} \n
                       ''')
    else:
        print("Error")
        
User()