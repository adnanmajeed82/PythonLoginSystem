import sys

fname = input("Enter first name")
lname = input("enter last name")

print(lname + "" + "" + fname)

print("Python version")
print(sys.version)
print("Version info")



def add_numbers(num1, num2):
    sum = num1+num2
    print("sum",sum)

def add_number():
    add_numbers(11,11)

add_number()