# CMPT 120 Intro to Programming
# Lab #4 – Working with Strings and Functions
# Author: Brian Kacsanik
# Created: 2019-02-25

def main():
    # get user's first and last names
    first = input("Enter your first name: ")
    last = input("Enter your last name: ")
    # TODO modify this to generate a Marist-style username
    uname = first + "." + last
    # ask user to create a new password
    passwd = input("Create a new password: ")
    # TODO modify this to ensure the password has at least 8
    characters = len(passwd)
    if characters < 8:
            print("Fool of a Took! That password is feeble!")
            passwd = input("Create a new password: ")
    print("The force is strong in this one…")
    print("Account configured. Your new email address is", uname + "@marist.edu")

main()
