input1 = input("please enter your name:")
input2 = input("please enter your surname:")
input3 = int(input("please enter your age:"))
input4 = int(input("please enter date of birth:"))

users_info =[input1,input2,input3,input4]
prewords=["Name","Surname","Age","Date of birth"]

print("\nUser's Information")
for i,j in zip(prewords,users_info):
    print(i,":",j)
if input3<18:
    print("You can not go out because it's too dangerous")
else:
    print("You can go out to the street.")