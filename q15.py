# My List Store
def add_mem(mem_list,mem_name):
    mem_list.append(mem_name)
    # return mem_list
def add_mems(mem_list,mem_names):
    mem_list.extend(mem_names)
    # return mem_list

#main
mem_list = list([])
print("Welcome to My Store:")
while(True):
    print("Press 1. To display all the members: \n Press 2. to add a new member: \n ")
    print("Press 3. to add multiple members: \n Press 4. to remove a member from the list: \n" )
    print("Press 5 to remove the last member from the list: \n Press 6 to find a member: ")
    res = int(input("Enter your response:")) 
    if(res ==2):
        mem_name  = input("Enter the name of the member:")
        add_mem(mem_list,mem_name)
    if(res == 3):
        mem_names = input("Enter the names of members")
        add_mems(mem_list,mem_names.split(","))
    if(res==4):
        del_name = input("Enter the name to be removed:")
        mem_list.remove(del_name)
        print(mem_list)
    if(res==5):
        mem_list.pop()
        print(mem_list)
    if(res==6):
        f_name= input("Enter the name to be found:")
        print(f_name in mem_list)
    if(res==1):
        print(list([mem_list]))
    ext = input("Do you want to Exit?")
    if(ext == "yes" or ext == "Yes"):
        break
        