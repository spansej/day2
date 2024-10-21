quantity = int(input("Enter the quantity you purchased: "))
cost = 100

if((quantity*cost)>1000):
    print("Total cost after 10% discount is ",(quantity*cost)-(quantity*cost*0.1))
else:
    print("Total cost is ",(quantity*cost))