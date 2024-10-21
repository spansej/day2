i=2
c=1
a=int(input("Enter a number"))
if(a==2 or a==3):
    print("Prime")
else:
    if(a%2!=0):
        while(i<=a/2):
            if(a%i!=0):
                c+=1
            i+=1
    if(c>1):
        print("Prime")
    else:
        print("Not Prime")