t1=float(input("enter a marks for test 1:"))
t2=float(input("enter a marks for test 2:"))
t3=float(input("enter a marks for test 3:"))
m=min(t1,min(t2,t3))
if t1==m:
    print("Average of best two test marks out of three test marks is",(t2+t3)/2)
elif t2==m:
    print("Average of best two test marks out of three test marks is",(t1+t3)/2)
else:
    print("Average of best two test marks out of three test marks is",(t2+t1)/2)
