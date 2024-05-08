print("Welcome to the Tip Calculator!")
price = (input("What was the Total Bill?\n$" ))
tip = input("How much Tip would you like to give? 10,12 or 15?\n")
people = int(input("How many People to Split the Bill?\n"))

price_int = float(price)
tip_int = (int(tip)/100)+1
people_int = int(people)

total_bill = price_int * (tip_int)
each_pay = round( total_bill / people_int,2)

message  = f"Each person should pay : ${each_pay}"
print(message)

