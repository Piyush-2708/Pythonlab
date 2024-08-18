from datetime import *
week=["MON","Tue","Wed","Thu","Fri","Sat","Sun"]
y=["January","Febraury","March","April","May","June","July","August","September","October","November","December"]
print(week[datetime.now().weekday()],y[datetime.now().month-1],datetime.now().day,datetime.now().time(),"IST",datetime.now().year)

