# Val Kyrvey Latoja
"""
Pizza Toppings

Chapter 6 Exercise 1
"""
prompt='what topping would you like on your pizza?'
while True:
    topping=input(prompt)
    if topping !='quit':
        print('ill add'+topping++'to your pizza.')
    else:
        break
#while means if the variable remains true it will function forever, while the break function breaks the while function. the if else function is nested.