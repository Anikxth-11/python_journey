choice=int(input('what do you want to choose? type 0 for rock, 1 for paper and 2 from scissors:\n'))
print(f'you chose: {choice}')
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
import random
if choice>=3 or choice<0:
    print('YOU TYPED AND INVALID NUMBER,YOU LOSE!')
else:
    game_images=[rock,paper,scissors]
    print(game_images[choice])
    random_choice=random.randint(0,2)
    print(f'computer chose: {random_choice}')
    print(game_images[random_choice])


    if choice== 0 and random_choice==2:
        print('YOU WIN!')
    elif random_choice>choice:
        print('YOU LOSE!')
    elif random_choice==choice:
        print('ITS A DRAW!')
    elif random_choice==0 and choice==0:
        print('YOU LOSE!')
    elif choice>random_choice:
        print('YOU WIN!')




