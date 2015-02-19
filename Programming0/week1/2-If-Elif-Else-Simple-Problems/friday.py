import time

today = time.strftime("%A")

if (today == "Friday"):
    print("It is %s" %(today))
else:
    print("It is not Friday ;( Today is %s" %(today))
