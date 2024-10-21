a = int(input("enter a number"))

for i in range(a):
    for k in range(i):
        print(" ",end="")
    # for j in range(a-i):
    print("*"*(2*(a-i)-1),end="")
    print("")

# for j in range(a*2-1,0,-2):
#         print(j)