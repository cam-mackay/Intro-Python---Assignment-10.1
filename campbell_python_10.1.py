#############################################
#Campbell Mackay                            #
#Intro Python - Assignment 10.1             #
#04 NOV 2018                                #
#############################################

import os #import the OS library

print("Welcome to the File Writing Program")

#ask user for directory, name of file, user name, user address, user phone number
#validate if directory exists using the OS library
directoryFlag = 0
while directoryFlag == 0:
    userDirectory = input("Enter directory to store file in: ")
    print("Validating directory...")
    if os.path.isdir(userDirectory):
        directoryFlag = 1
        print("Chosen directory exists")
    else:
        directoryFlag = 0
        print("Chosen directory does not exist, try again.")

userFileName = input("Enter name of file to store in directory: ")

userName = input("Enter your name: ")

userAddress = input("Enter your address: ")

userPhoneNumber = input("Enter your phone number: ")

#write user data to file; store file to chosen directory
try:
    print("Writing file...")
    with open(userFileName, 'w') as fileHandle:
        fileHandle.write(userName + "," +
                         userAddress + "," +
                         userPhoneNumber)

    print("Your file, " + userFileName + ", has been stored in the specified directory.")
except:
    print("An error occurred while attempting to store file in specified directory.")

#read the file and display the contents for user to validate
try:
    print("Reading file...")

    with open(userFileName, 'r') as fileHandle:
        userFileData = fileHandle.readline()

    print(userFileData)
except:
    print("An error occurred while attempting to read stored file.")
