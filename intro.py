#this is a single line commment

"""
This is
a  multi line
comment
"""

#this is print function in pyhton
"""
print("Hello batch ")

print(2 + 2)

#button calling
def dial(phone_num):
    print(f"{phone_num} \n Calling ...")

def openDialer(num_length,user_provided_num):
    if user_provided_num > 10 or type(user_provided_num)==str:
        print("Number invalid")
    elif user_provided_num < 10:
        print("Call Ended")
    elif user_provided_num == 10 and type(user_provided_num)==int:
        dial(user_provided_num)
    else:
        return

recipent_num = input("Please Provide number: ")
openDialer(len(recipent_num),recipent_num)
"""
#string formatting
#age = input("Enter your age :")
#name = input("Enter your name :")
#print(f"hi! your name is {name} you are {age} years old")

