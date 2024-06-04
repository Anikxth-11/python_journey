print('WELCOME TO THE ROLLER COASTER RIDE!!')
height=int(input('please enter your height in centimeters:\n'))
bill = 0
if height > 120:
    print('you are allowed to enter the rollercoaster ride\n please collect the tickets from the next counter!!')
    age=int(input('enter your age:\n'))
    if age<=18:
        bill = 10
        print("your ticket cost is 10 rupees")
    
    else:
        bill = 30
        print("your ticket price is 30 rupees")
        
    want_photo = input('do you want a photo with your ticket? Y OR N')
    if want_photo == "Y" :
        bill +=5
        print(f'your total bill is rupees {bill}')
        
        
else:
    print('sorry you are not allowed to enter beacuse the height requirement is not fulfilled\n\nTHANK YOU VISIT AGAIN!!')


    


