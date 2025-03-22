

def newtonsMethod(usrNum, usrApprox):
    
    iteration = 1
    x0 = 0
    error = .00000001
    while True:
        x1 = ((usrApprox + (usrNum / usrApprox)) / 2 )
        usrApprox = x1
        print(f"Iteration: {iteration} = {x1}")
        
        if abs(x1 - x0) < error:
            print("Root found to be approximately: ", x1)
            
            return
        
        x0 = x1
        iteration += 1
       


usrNum = int(input("Enter the number you want to approximate the square root of: "))
usrApprox = int(input("Enter the number you want as a reasonable guess of the square root (int): "))

newtonsMethod(usrNum, usrApprox)


