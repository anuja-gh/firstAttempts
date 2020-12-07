import random

h=0
t=0
i=1

while i<=100:
    count=random.randint(0,1)
    if count==0:
        h+=1
    else:
        t+=1
    i+=1

print("heads for :"+ str(h))
print("tails for :"+str(t))


