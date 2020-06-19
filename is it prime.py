
divisors = 0

userinput = input ("Please enter a integer: ")
userinput = int (userinput)

while True:
    for i in range (1,userinput,1):
        i = divisors+1
    
    try:
        if divisors<2:
            print ("This number is prime")
            break
        if divisors>2:
            print ("This number is not prime")
            break
        if userinput==1:
            print ("1 is prime")
            break
        if userinput==0:
            print ("0 is prime")
            break


    except:
             print("invalid int, please enter a proper god daym int")
