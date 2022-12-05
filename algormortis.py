#Algor Mortis Calculator for Forensic Science 

#Temp Loss
tempLoss = 0
#Keeps program looped
isLoop = 1

#Introduction Function
def intro():
    #Fancy Intro & Developer Credit Stuff
    print("/////////////////////////////////////////")
    print("This Program was made by Andrew Glidden on November 3rd, 2022 and all credits belong to them.")
    print("It's sole purpose is for educational and recreational use to calculator algor mortis efficently.")
    print("You are permitted to redistribute, modify or copy any parts of this program as you wish.")
    print("All rights to this program have been reliquished by the sole owner.")
    print("/////////////////////////////////////////")
    
#Main Function
def main():
    global tempLoss
    
    #Asks for the temperature of the body
    print("\nWhat is the current temperature of the body in degrees celsius?")
    bodyTemp = float(input("--> ")) 
    
    #Normal Body Temperature 
    normalTemp = 37 #degrees celsius
    
    #Amount of degrees lost
    tempLoss = normalTemp - bodyTemp 
    
    #T.O.D
    timeSince = 0     
    
    #Calls determine() function
    determine()

#Function for doing calculations if 12 hours has not passed
def formula():
    global normalTemp
    global tempLoss
    global timeSince
    
    #Assigns a variable timeSince the value of the loss of temperature divided by 0.78 (the temperature loss in the first 12 hours)
    timeSince = tempLoss / 0.78
    
    #Defines the interger value of the result of timeSince as the hours
    hours = int(timeSince)
    
    #Defines the decimal value of timeSince as the minutes and converts it into the proper form
    minutes = (timeSince - hours) * 60
    
    #Prints the final result 
    print("\nThe body has been dead for",hours, "hours","and", minutes, "minutes.")
    
    #Prevents program from closing until the user hits enter
    input()
    
#Function for doing calculations if at least 12 hours has passed
def formula12():
    global normalTemp
    global tempLoss
    global timeSince
    
    #Assigns a variable timeSince the value of the loss of temperature divided by 0.78 (the temperature loss in the first 12 hours)
    timeSince = (tempLoss - 9.36) / 0.39
    
    #Defines the interger value of the result of timeSince as the hours
    hours = int(timeSince)
    
    #Defines the decimal value of timeSince as the minutes and converts it into the proper form
    minutes = (timeSince - hours) * 60
    
    #Prints the final result 
    print("\nThe body has been dead for",hours + 12, "hours","and", minutes, "minutes.")
    
    #Prevents program from closing until the user hits enter
    input()
    
def determine():
    global tempLoss
    
    #Determines if at least 12 hours have passed since T.O.D
    if tempLoss >= 9.36:
        formula12()
    else:
        formula()
    
intro()
while isLoop == 1:
    main()