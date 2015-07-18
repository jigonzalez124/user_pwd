##  Name:           Jesus Ivan Gonzalez
##  Create Date:    July 18th 2015
##  Description:    User/Password Setup.  Uses a text file with list of users & passwords

fhandle = open("UserPwdStorage.txt")
userName = input("Enter user name: ")

foundUser = 0;      #seeks if username exists
for line in fhandle:
    spaceLoc = line.find(" ") + 1
    correctUser = line[:spaceLoc].strip()
    if (userName == correctUser):   #true if user name exists
        foundUser = 1;
        passwordCorrect = line[spaceLoc:].rstrip()  #retrieve correct password
        passwordInput = input("Enter your password: ")  #inputs password from user

        tries = 0
        while(True):
            if (passwordCorrect == passwordInput):  #if match, then access
                print("Welcome!  You got your username/password right!")
                break;
            elif tries == 3:    #locks out after three tries
                print("You have been locked out.")
                break;
            else:
                tries += 1
                if tries < 3:   #ask again 
                    print("Incorrect.  Try again.")
                    passwordInput = input("Enter your password: ")
        break

if foundUser == 0:      #true if no user exists
    print("No user exists.")
