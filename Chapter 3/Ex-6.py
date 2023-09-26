# Val Kyrvey Latoja
"""
Shrinking Guest List

CHapter 3 Exercise 6
"""

print("Due to inconveniences, I am unfortunately invting only two guests for tonight's dinner.")

Guests= ["Sister","Mother","Aunt","Cousin","Co-worker"]

print("\nPrevious Guest list:")
for name in Guests:
    print(name)
# take note if you removed a variable, the next variable will take its place so for the next line you just take out the variable who took the spot.
Guests.pop(2)
Guests.pop(2)
Guests.pop(2)

print("\nCurrent Guest list:")
for name in Guests:
    print(name)

print("\nMy",Guests[0],", You are invited to my dinner for tonight.")
print("My",Guests[1],", You are invited to my dinner for tonight.")



del Guests[0]
del Guests[0]
# doing this stuff below t ofeel fancy
if not "Sister" in Guests:
    print("\nList is now empty.")