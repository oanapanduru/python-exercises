# -*- coding: utf-8 -*-
"""
Created on Wed Jul 29 21:50:29 2020

@author: oanap
"""
total_cost = int(input('total cost:'))
annual_salary = int(input('annual salary:'))
portion_saved = float(input('portion saved:'))
semi_annual_raise = float(input('raise:'))
r = 0.04
portion_down_payment = 0.25*total_cost
print(portion_down_payment)
monthly_salary = int(annual_salary)/12
print(monthly_salary)
months = 0
monthly_saving = portion_saved*monthly_salary
current_saving = 0
print(monthly_saving)
while current_saving <= portion_down_payment:
    current_saving = monthly_saving + (current_saving*r/12) + current_saving
    print(current_saving)
    months +=1
    print(months)
    if months%6 == 0:
        monthly_salary = monthly_salary + (monthly_salary*semi_annual_raise)
        monthly_saving = portion_saved*monthly_salary
        print(monthly_salary)


