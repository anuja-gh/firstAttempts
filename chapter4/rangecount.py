print("This is your game")

start=int(input("Enter your start limit:"))
end=int(input("Enter the end limit:"))

mid=int(input("whats the multiplication range:"))

for i in range(start,end,mid):
    print(i,end=' ')
