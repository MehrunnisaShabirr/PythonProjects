def show():
    global email
    print("Verify your email constraints here...")
    email = input("Enter the email:")

def limits():
    if len(email)>=8:
        pass
        if email[0].isalpha():
            pass
            for i in email:
                if ('@' in email) and (email.count('@')==1):
                    continue
            else:
                print("Email should contain one '@' symbol!")
                if email[-4]==".":
                    pass
                else:
                    print("The correct email format is:\nxyz@gmail.com\nThere should be a dot!")
                    for j in email: 
                        if j == j.isalpha():
                            continue
                        elif j == j.isspace():
                            print("There should be no space in an email!")
                        elif j == j.lower():
                            continue
                        elif j == j.upper():
                            print("NO uppercase letters are allowed!")
                        elif j == "_" or j == "." or j == "@":
                            continue
                        else:
                            print("No symbols are allowed")
                        print("Your email is valid!")
                        again()
                    
        else:
            print("The first letter should be an alphabet!")
    else:
        print("Email should have more than 8 characters!")

def again():
    choice = input("Do you wanna check more emails? \n(y/n): ")
    if choice.upper()=="Y":
        show()
        limits()
    elif choice.lower()=="n":
        print("Ok bye!\nHave a nice day!")
    else:
        print("Please enter 'y' or 'n' ...")

show()
limits()
