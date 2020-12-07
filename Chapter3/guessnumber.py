
guess_limit=3
static=100
i=1
while i<=guess_limit:
    guess=int(input("guess the number:"))
    if guess==static:
        print("you are awesome!!")
        break
    i+=1
    if i<=guess_limit:
        continue
    else:
        print("done with guess limit")
