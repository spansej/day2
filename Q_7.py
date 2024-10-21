def add(a,b):
    return (a+b),(a**2),(a**b)
while(True):
    a=int(input("Enter a number: "))
    b=int(input("Enter second number: "))
    c = add(a,b)
    print("Addition, Square, Exponenation of two numbers is: ",c[0],c[1],c[2])
    if('exit' == input("Enter exit to exit or Any other  to continue: ").lower()):
        break
