print('welcome to the tip calculator')
bill=float(input('how much was the total bill?₹'))
tip=int(input("select the percentage of tip you want to give\n 10\n 15\n 20\n "))
people=int(input('how many people do you want to split the bill between?'))
bill_with_tip = round(bill/100 *bill + bill)
print(f'each person should split the bill and give ₹{bill_with_tip}')
print('THANK YOU VISIT AGAIN!!')

    



