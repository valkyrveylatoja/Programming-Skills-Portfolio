prompt="how old are you?"
while True:
    age=input(prompt)
    if age=='quit':
        break
    age=int(age)
    
    if age <3:
        print('you get in free!')
    elif age<13:
        print('your ticket will be $10.')
    else:
        print('your ticket is $15.')
#using if, elif, and else nested function from the while true function. this can only work if the user answers with an integer answer.
