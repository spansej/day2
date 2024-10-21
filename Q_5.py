class_held = int(input("Enter the number of classes held: "))
class_attend = int(input("Enter the number of classes attend: "))

if((class_attend/class_held)>=0.75):
    print("Allowed to sit in exam")
else:
    print("Not allowed to sit in exam.")

# '''using ternary operator'''
# print("Allowed to sit in exam") if ((int(input("Enter the number of classes attend: "))/int(input("Enter the number of classes held: ")))>=0.75) else print("Not allowed to sit in exam.")