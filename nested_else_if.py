print('WELCOME TO THE ROLLER COASTER RIDE!!')
height=int(input('please enter your height in centimeters:\n'))
if height > 120:
    print('you are allowed to enter the rollercoaster ride\n please collect the tickets from the next counter!!')
    age=int(input('enter your age:\n'))
    if age<=18:
        print("your ticket cost is 10 rupees")
    else:
        print("your ticket price is 30 rupees")
        
else:
    print('sorry you are not allowed to enter beacuse the height requirement is not fulfilled\n\nTHANK YOU VISIT AGAIN!!')


    


