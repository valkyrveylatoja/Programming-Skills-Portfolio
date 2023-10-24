# Val Kyrvey Latoja
"""
River

Chapter 5 Exercise 4
"""
rivers={
        'the nile river': 'egypt',
        'yenisei': 'mongolia',
        'ob': "russia"
        }
for river, country in rivers.items():
    print(" the"+ river.title()+" is at"+country.title())
print("\nthe following rivers are included in this date set:")
for river in rivers.keys():
    print("-"+river.title())
print("\nthe following countries are included in this date set:")
for river in rivers.values():
        print("-"+river.title())
#a more extended version of the for and in fucntions