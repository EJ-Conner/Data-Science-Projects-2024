



def myFind(usrStr, usrChar):
    i = 0
    print("Indices where letter is found: ", end = ' ')
    for x in range(len(usrStr)):
        if usrStr[x] == usrChar:
            print( x, end = ' ')
            i +=1
    print("\nTotal times caharacter found: ", i)
    return 

usrStr = input("Enter a string: ")
usrChar = input("Enter a single character: ")

myFind(usrStr, usrChar)

