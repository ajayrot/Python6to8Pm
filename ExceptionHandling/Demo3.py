
try:
    no1 = int(input("1st No :"))
    no2 = int(input("2nd No :"))
    print("The Sum = ",no1+no2)
    print("The Div = ",no1/no2)
    print("The sub = ",no1-no2)
    print("The Mul = ",no1*no2)
except ValueError:
    print("Invalid Input")
except ZeroDivisionError as zde:
    print("Your are : ",zde)
    print("The sub = ", no1 - no2)
    print("The Mul = ", no1 * no2)

print("Thanks")