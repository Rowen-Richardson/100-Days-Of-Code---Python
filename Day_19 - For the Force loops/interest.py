#Mini challange Loan Amount

loan_amount = 1000

for payments_year in range(25):
  interest = 5 / 100
  loan_amount += (loan_amount * interest)
  print("Year", payments_year + 1, "your payment is: R",round(loan_amount,2))


