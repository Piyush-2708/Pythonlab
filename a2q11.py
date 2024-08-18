sen=input("enter a sentence:")
a=sen.split()
print("This sentence has",len(a),"words")
digit,up,low=0,0,0
for i in a:
    for j in i:
        if ord(j) in range(48,58):
            digit+=1
        elif ord(j) in range(65,91):
            up+=1
        elif ord(j) in range(97,123):
            low+=1

print("this sentence has",digit,"digits")
print(up,"upper case letters")
print(low,"lower case letters")
            
