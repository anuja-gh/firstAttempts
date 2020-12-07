basePrice=float(input("Enter the base price of Grand i10 sportz: "))

tax= basePrice*5/100
lisence=basePrice*3/100
dealerPrep=10000
destinationCharge=12000
onroadPrice=tax+lisence+dealerPrep+destinationCharge
print("The on road actual price of the car is:"+str(onroadPrice))
