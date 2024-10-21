while(True):
    num = int(input("Enter the number: "))
    if(num%3==0 and num%5==0):
        print("Fizz Buzz")
    elif(num%3==0):
        print("Fizz")
    elif(num%5==0):
        print("Buzz")
    else:
        print("Invalid Input")
    if('exit' == input("Enter exit to exit or Any other  to continue: ").lower()):
        break

