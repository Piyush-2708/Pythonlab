n=int(input("enter first number:"))
m=int(input("enter second number:"))
k=int(input("enter third number:"))
if n>=m and n>=k:
    print(n,"is largest")
elif m>=n and m>=k:
    print(m,"is largest")
else:
    print(k,"is largest")
