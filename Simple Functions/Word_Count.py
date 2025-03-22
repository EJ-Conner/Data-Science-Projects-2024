

def countWords(usrStr):
    wordCount = 1
    for x in range(len(usrStr)):
        
        if ord(usrStr[x]) == 32 and ord(usrStr[x+1]) != 32:
            wordCount +=1

    return wordCount

usrStr = input("Enter a string: ")

print("Words in the string: ", countWords(usrStr))
