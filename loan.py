import math
car_name=input("Enter car name :")
car_type=input("Enter car type :")
price_car=int(input("Enter price of car :"))
first_payment=int(input("Enter amount you paid :"))
bank_interest_rate =int(input("Enter the bank intrest :"))
no_of_years_pay=int(input("Enter no of yr to pay :"))

 # balance amount to pay as emi(car parice -paid amount)(E = P x R x (1+r)n/((1+r)N –1)
amount_pay= price_car-first_payment#p
#to equal the price by month
rate_of_month= ((bank_interest_rate)/12)/100#r
no_of_months_pay=no_of_years_pay*12#n(N)
#apply in formula
  
emi= (amount_pay*rate_of_month*((1+rate_of_month)**no_of_months_pay))/(((1+rate_of_month)**no_of_months_pay)-1)

print("")
print("")
print(f"car name :"           ,car_name)
print(f"car type :"           ,car_type)
print(f"price of car :"       ,price_car)
print(f"on time payment :"    ,first_payment)
print(f"bank interest rate :" ,bank_interest_rate)
print(f"years to pay :"       ,no_of_years_pay)
print(f"months to pay :"      ,no_of_months_pay)
print(f"blance amount :"      ,amount_pay)

print("amount to pay every month :",math.ceil (emi))
