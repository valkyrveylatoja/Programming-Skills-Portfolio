# Val Kyrvey Latoja
"""
Print Date and Time

Chapter 1 Exercise 3
"""
# do line 8 in order to do this
from datetime import datetime

dateandtime = datetime.now()
DateAndTime = dateandtime.strftime("%d/%m/%Y %H:%M:%S") # modifying variables from dateandtime
print("Current Date and Time =", DateAndTime) #then print