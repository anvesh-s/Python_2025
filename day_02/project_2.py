print("Welcome to the tip calculators")
initial_bill = float(input("what was the total bill? "))
#print(type(initial_bill))
tip = int(input("How much tip would you like to give? 10,12, or 15? "))
bill_with_tip = tip/100*initial_bill + initial_bill
number_of_people = int(input("how many people to split the bill? "))
print((initial_bill +bill_with_tip) / number_of_people )
