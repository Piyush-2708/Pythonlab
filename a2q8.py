a=float(input("enter first side length:"))
b=float(input("enter second side length:"))
c=float(input("enter third side length:"))
m=max(a,max(b,c))
if a==m:
    if a**2==(b**2)+(c**2):
        print("yes it is a right angled triangle")
elif b==m:
    if b**2==(a**2)+(c**2):
        print("yes it is a right angled triangle")
else:
    if c**2==(b**2)+(a**2):
        print("yes it is a right angled triangle")
