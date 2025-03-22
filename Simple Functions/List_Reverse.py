

def reverse(inputList):
    front = 0
    end = len(inputList) - 1
    while front < end:
        inputList[front], inputList[end] = inputList[end], inputList[front]
        front += 1
        end -= 1
        
    return inputList

li = [0, 4, 9, 4, 8, 'world', 15, 4, 'Hello', -0.9]
print(f"List before: {li}")
print(f"List after reversing: {reverse(li)}")
