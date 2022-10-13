# Functions - Sets of line of statements which performs a specific task.

# Code Reusuability is the main feature of function.

# a=76
# b=21


# print(a+b)
# print(a-b)
# print(a*b)
# print(a/b)

# a=12
# b=15

# print(a+b)
# print(a-b)
# print(a*b)
# print(a/b)


# def  -- Its the keyword for declaring the functions.
"""
def functionname():
    statements
"""


# a=76
# b=21

# def basic_ops():
#     print(a+b)
#     print(a-b)
#     print(a*b)
#     print(a/b)


# # Calling the declared function is very important. Without function call no single line in the function will be executed..

# basic_ops() # function call.

# print(a)
# print(b)

# a=12
# b=15

# basic_ops()

# print(a)
# print(b)

# def basic_ops(a,b):
#     print("A value",a)
#     print("B Value",b)
#     print(a+b)
#     print(a-b)
#     print(a*b)
#     print(a/b)


# basic_ops(76,21)
# print(a)
# print(b)

# basic_ops(12,15)
# print(a)
# print(b)

# Passing Arguments to the function(5 Ways):
    # 1) Positional Arguments - Assigning the values to the arguments inside the function based on the position of values based at function call.
    # 2) Default Arguments - Passing a default value to a argument at the function declaration itself. 
            # If any value is passed to the argument at the function call,Default value will be updated with the passed value.
            # If no value is passed to the argument at the function call, Default value will e taken into consideration..
    # 3) Keyword Arguments
    # 4) Arbitrary Positional Arguments
    # 5) Arbitrary Keyword Arguments


# def Employee_info(name,email,company):
#     print("HI {}, your email id {} is successfully registered with {}.".format(name,email,company))


# Employee_info("Rajesh","Rajesh@gmail.com","Wipro")

# Employee_info("Rajesh@gmail.com","Wipro","Rajesh")

# Employee_info("Suresh","Suresh@gmail.com") # Throw the error as no.of argument declared and no.of values passed is not matching.


# 2) Default arguments:
    #  Passing a default value to a argument at the function declaration itself.


# def Employee_info(name,email,company="",worklocation="Pune"):
#     print("HI {}, your email id {} is successfully registered with {} and your work location is {}.".format(name,email,company,worklocation))


# Employee_info("Venkat","venkt@gmail.com","Wipro","Hyderabad")

# Employee_info("Venkat","venkt@gmail.com","","Chennai")

# 3) Keyword Arguments: Declaring the value to the argument at function call using argument name.


# def Employee_info(name,email,company,worklocation):
#     print("HI {}, your email id {} is successfully registered with {} and your work location is {}.".format(name,email,company,worklocation))


# Employee_info(name="Mahesh",company="Infosys",worklocation="Delhi",email="Mahesh@gmail.com")

# Employee_info("Basha","Basha@gmail.com",company="Microsoft",worklocation="Gurgoan")


# # Employee_info("L&T","Basha@gmail.com",name="Basha",worklocation="Gurgoan") # Thrown an error as multiple value will be passed to "name" argument..

# # Employee_info(name="Basha","Basha@gmail.com",company="L&T",worklocation="Gurgoan") # Thown an error, as positional argument is declared after keyword argument.

# 4) Arbitrary Positional Arguments: Passing multiple positional argument at the function call..

# * -- Its the symbol used for Arbitrary Positional declaration

# def credit_trans(*trans):
#     print(trans)
#     total = 0
#     for ele in trans:
#         total = total + ele

#     print("Hi,Your credit card bill for this month is ",total)

# credit_trans(546.56,1234.65,7686)

# credit_trans(7685,6454,876,6533)

# credit_trans(874,968,13442,6546,8754)

# 5) Arbitrary Keyword Arguments: Passing multiple keyword arguments at the function call..

# ** -- Its the symbol used for Arbitrary Keyword declaration
# def credit_trans(**trans):
#     print(trans)
#     # print(type(trans))
#     dict_len = len(trans)
#     total = 0
#     for ele in trans:
#         if ele == 'name':
#             continue
#         total += trans[ele]
    
#     print("Hi {}, you credit card bill for {} months is {}".format(trans['name'],dict_len,total))

# credit_trans(jan=5334,feb=7659,name="rajesh")
# credit_trans(mar=7843,name="mahesh",april=7484,may=4647)

# credit_trans(june=5453,july=6473,name="venkat",aug=5463,sep=8844)

# def credit_trans(*trans,**info):
#     print(trans)
#     print(info)
#     total = sum(trans)

#     print("HI {}, your crdit card bill statement of amount {} has been sent to {} email address".format(info['name'],total,info['email']))

# credit_trans(6574,4352,7565,name="rajesh",email="rajesh@gmail.com")


name = "Rajesh" # global variable

def info(email):
    print(email) # local varibale
    mobile = 54436437633 # local varibale
    print(mobile)
    print(name)

info("rajesh@gmail.com")

print(name)

print(email)