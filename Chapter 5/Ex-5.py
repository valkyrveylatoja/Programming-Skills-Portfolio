# Val Kyrvey Latoja
"""
Pets

Chapter 5 Exercise 5
""" 
pets=[]
pet={
     'animal type': 'dog',
     'name': 'max',
     'owner': 'val',
     'weight': 43,
     'eats': 'meat'
     }
pets.append(pet)

pet={
     'animal type': 'cat',
     'name': 'vanessa',
     'owner': 'val',
     'weight': 37,
     'eats': 'fish'
     }
pets.append(pet)
for pet in pets:
    print('\nmy pet named,'+pet['name'].title()+":")
    for key, value in pet.items():
        print("\t"+key+": "+str(value))
#using the .append function to add the already empty list from line 1