

def myToUpper(usrStr):
    upperCaseList = []
    for x in range(len(usrStr)):
        
        if ord(usrStr[x]) >= 97 and ord(usrStr[x]) <= 122:
            upperCaseList.append(chr(ord(usrStr[x])-32))
        else:
            upperCaseList.append(usrStr[x])
    print("List after changing to uppercase")
    for x in range(len(upperCaseList)):
        print(upperCaseList[x], end = '')
    print()

usrStr = input("Enter a string: ")
list(usrStr)
print("List before changing to uppercase")
for x in range(len(usrStr)):
        print(usrStr[x], end = '')
print()

myToUpper(usrStr)

