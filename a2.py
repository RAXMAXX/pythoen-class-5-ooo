actual_cost = float(input("Please Enter The Actual Procduct Price:"))
sale_amount = float(input("Please Enter the Sales Amount:"))

if (sale_amount > actual_cost):
    profit = sale_amount - actual_cost
    print("Total profit =",profit)
elif (actual_cost > sale_amount):
    loss = actual_cost - sale_amount
    print("Total Loss = ",loss)
else:
    print("No profit and loss")