from datetime import datetime
import datetime as dt
now = datetime.now()
current_time  = now.strftime("%H:%M:%S")
x = dt.time(17, 18, 20)

print(type(current_time))
print(type(str(x))) 
print(current_time)
print(x) 

if current_time == str(x):
    print("YES")
else:
    print("NO")