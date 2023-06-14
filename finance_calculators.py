# Level1 Task 11 - Capstone Project 1 (Variables and control structures)
# Knowledge from Level 1 previous tasks have been applied such as logical operations, if els statements, f-strings, math functions

import math

#the code will convert user input to lowercase. Also multple lines are used for notes by adding '''
choose_calculation_type = input('''Choose either 'investment' or 'bond' from the menu below to proceed:
investment - to calculate the amount of interest you'll earn on your investment        
bond       - to calculate the amount you'll have to pay on a home loan\n''').lower()  
                                                                                     
if choose_calculation_type=="investment":
    money_deposited = float(input("Deposit amount(R): "))
    interest_rate_invest = float(input("Enter interest rate(%): "))
    years_invested =int(input("Enter investment period(years): "))
    interest = input("Do you want 'simple' or 'compound' interest? \n").lower()  #the code will convert whatever sentence case is used to lowercase
    if interest=="simple":
        A_simple = money_deposited*(1+((interest_rate_invest/100)*years_invested))
        print(f"You will have R{round(A_simple,2)} in {years_invested} years.")
    elif interest=="compound":
        A_compound = money_deposited*math.pow((1+(interest_rate_invest/100)),years_invested)
        print(f"You will have R{round(A_compound,2)} in {years_invested} years.")

# I tried entering 20 years at 8% interest on R100 000. With simple interest you will get: R260 000. With compound interest you will get: R466 095.71. It is clear that investing with compound interest is better. 

# It was assumed there will be no lump sum payments.    
elif choose_calculation_type=="bond":
    present_house_val = float(input("Enter the present value of the house(R): "))
    interest_rate_bond = float(input("Enter interest rate(%): "))
    repay_months = int(input("Enter bond repayment period(months): "))
    repayment =((interest_rate_bond/(12*100))*present_house_val)/(1-(1+(interest_rate_bond/(12*100)))**(-repay_months))
    print(f"You have to pay R{round(repayment,2)} monthly.")
    
else:
    print("Please select an item from the menu!")
    
#choose_calculation_type=="investment" or choose_calculation_type=="Investment" or choose_calculation_type=="INVESTMENT" --- wastes time. Just use .lower() in input
#choose_calculation_type=="bond" or choose_calculation_type=="Bond" or choose_calculation_type=="BOND"
