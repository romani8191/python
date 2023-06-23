print("hi, there How r u?")
a=input("Are you an old user or a new one: ")
print (a)
bill=int(1000)

if (a==str("old")):
    print("total discount is 10%")

    b=input("Do you have a disount coupon?: (y/n)")
    print(b)
    if(b==str("y")):
        print ("total discount is 20%")
        netAmount = bill
        print(f"Your total bill is : {netAmount} without discount")
        print ("after discount")
        amount= bill- int((20/100) * bill)
        print(f"Your total bill is : {amount}")
    else:
        print("stay updated with us for discount coupons")
        netAmount = bill
        print(f"Your total bill is : {netAmount} without discount")
        amount = bill - int((10 / 100) * bill)
        print ("after discount")
        print(f"Your total bill is : {amount}")


elif (a==str("new")):
    print("total discount is 30%")

    b = input("Do you have a disount coupon?: (y/n)")
    print(b)
    if (b == str("y")):
        print("total discount is 60%")
        amount = bill - int((60 / 100) * bill)
        netAmount = bill
        print(f"Your total bill is : {netAmount} without discount")
        print ("after discount")
        print(f"Your total bill is : {amount}")
    else:
        print("stay updated with us for discount coupons")
        amount = bill - int((30 / 100) * bill)
        netAmount=bill
        print(f"Your total bill is : {netAmount} without discount")
        print ("after discount")
        print(f"Your total bill is : {amount}")



