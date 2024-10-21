# a =0
# b= 1
# c=a+b
# n = int(input("Enter a number"))
# print("Fibonacci Series")
# print(a , end=" ")
# if(n!=0):
#     print(b, end=" ")
# while(True):
#     c=a+b
#     a=b
#     b=c
    
#     if(c>n):
#         break
#     print(c,end=" ")

# print("\n")

a=0
b=1
n=int(input("Enter a number"))
print("Fibonacci Series")
while(a<=n):
    print(a)
    a,b=b,a+b
print("\n")