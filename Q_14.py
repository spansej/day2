i=1
s=0
a=int(input("Enter a number: "))
print("Odd numbers")
while(i<=a):
    if(i%2==0):
      s=s+i
    i+=1

print("Sum of even numbers :",s)