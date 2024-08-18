for i in range(2,20):
    c=0;
    j=2;
    while j<i:
        if i%j==0:
            c=1
            break
        j+=1
    if c==0:
        print(i,"is a prime number")
