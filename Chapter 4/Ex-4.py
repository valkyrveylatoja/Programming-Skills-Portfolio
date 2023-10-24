# Val Kyrvey Latoja
"""
Stages of Life

Chapter 4 Exercise 4
"""
age=int(input('Please tell me your age:'))
if age<2:
    print('You are a baby.')
elif age<4:
    print('You are a toddler.')
elif age<13:
    print('You are a kid.')
elif age<20:
    print('You are a teenager.')
elif age<65:
    print('You are an adult.')
else:
    print('You are an elder.')
#here is an expansive use of the elif function, using many variables and using relational operators can also be combines when in the use of an elif function.