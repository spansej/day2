percentage = float(input("Enter the percentage: "))
if(percentage>100):
    print("Cannot be more than 100")
else:
    if(percentage>80):
        print("Grade: A")
    elif(percentage>60 and percentage<=80):
        print("Grade: B")
    elif(percentage>50 and percentage<=60):
        print("Grade: C")
    elif(percentage>45 and percentage<=50):
        print("Grade: D")
    elif(percentage>25 and percentage<=45):
        print("Grade: E")
    else:
        print("Grade: F")