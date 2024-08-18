choice=int(input("enter your choice 1 for celsius and 2 for Farenheit:"))
temp=float(input("enter temp:"))
if choice==1:
    print("given temp in celsius is:",temp)
    print("given temp in farenheit is:",(temp/5)+32/9)
else:
    print("given temp in Farenheit is:",temp)
    print("given temp in celsius is:",5*(temp-32/9))
