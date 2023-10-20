sandwich_orders=['tuna','ham and cheese','veggie']
finished_sandwiches=[]
while sandwich_orders:
    current_sandwich=sandwich_orders.pop()
    print('im working on your '+current_sandwich+'sandwich.')
    finished_sandwiches.append(current_sandwich)
print("\n")
for sandwich in finished_sandwiches:
    print('i made a '+sandwich+'sandwich.')
#though this looks comples, we are only appending the finished sandwiches list in the while function, then we print of what new sandwich is added.