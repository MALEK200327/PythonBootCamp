BillAmount = input("enter the amount of the bill\n")
Tips = input("enter tips 10 12 15\n")
NumberOfPeople = input("number of people to split the bill\n")
Taxes=0.12
TotalAmount = float(BillAmount) + float(Tips) + (float(BillAmount) * Taxes)
EachPerson = TotalAmount/float(NumberOfPeople)
print("Each person should pay: ", round(EachPerson,2)) 