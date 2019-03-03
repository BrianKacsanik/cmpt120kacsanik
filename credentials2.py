# main function?
def getname():
    first = input("Enter your first name: ")
    last = input("Enter your last name: ")
    return [first, last]

name = getname()

def username():
    return name[0] + "." + name [1]

uname = username()

def password():
    passwd = input("Create a new password: ")
    characters = len(passwd)
    if characters < 8: # password validation function?
        print("Fool of a Took! That password is feeble!")
        passwd = input("Create a new password: ")
    return [passwd]

password()
print("Account configured. Your new email address is", uname + "@marist.edu")
