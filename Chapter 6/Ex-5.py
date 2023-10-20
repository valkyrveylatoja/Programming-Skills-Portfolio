sandwich_orders=['ham and cheese','peanut butter and jelly','pastrami']
finished_sandwiches=[]
print('im sorry, were all out of ham and pastramy today.')
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')
print('\n')
while sandwich_orders:
    current_sandwich=sandwich_orders.pop()
    print('im working on your '+current_sandwich+' sandwich.')
    finished_sandwiches.append(current_sandwich)
print('\n')
for sandwich in finished_sandwiches:
    print('i made a '+sandwich+' sandwich.')
#a more extended version of exercise 4.