
car_price = 155368
onspot_payment = 1600
loanmoney_pay = car_price - onspot_payment

annual_interest_rate = 7.0 
monthly_interest_rate = annual_interest_rate / 12 / 100

loanperiod_years = 5
loan_period_months = loanperiod_years * 12


emi = (loanmoney_pay * monthly_interest_rate * (1 + monthly_interest_rate) ** loan_period_months) / \
      ((1 + monthly_interest_rate) ** loan_period_months - 1)


total_payable = emi * loan_period_months


print(f"Total Loan Amount: {loanmoney_pay:,}")
print(f"Monthly EMI: {emi:}")
print(f"Total Payable Amount: {total_payable:}")
