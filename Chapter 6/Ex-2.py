# Val Kyrvey Latoja
"""
Movie Tickets

Chapter 6 Exercise 2
""" 
prompt="How old are you?"
while True:
    age=input(prompt)
    if age=='quit':
        break
    age=int(age)
    
    if age <3:
        print('You get in free!')
    elif age<13:
        print('Your ticket will be $10.')
    else:
        print('Your ticket is $15.')
#using if, elif, and else nested function from the while true function. this can only work if the user answers with an integer answer.
