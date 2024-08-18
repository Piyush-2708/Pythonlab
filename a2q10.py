n=input("enter a number:")
if n==n[-1::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")
a=[]
for i in n:
    if i in a:
        pass
    else:
        a.insert(len(a),i)
        print(i,"appears",n.count(i),"times")

    

