import time
timestamp=time.strftime('%H:%M:%S' )
print(timestamp)
a=int(time.strftime('%H'))
if(a==12 or a<12):
    print("Good Morning")
elif(a>12 and a<16):
    print("Good Afternoon")
else:
    print("Good Evening")