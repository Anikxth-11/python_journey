
from random import randint


easy_turns=10
hard_turns=5
def difficulty():
    LEVEL=input("what level of difficulty would you like to choose? type 'easy' or 'hard': ")
    if LEVEL == "easy":
      return easy_turns
    else:
        return hard_turns
    
def game():
    print("WELCOME TO THE NUMBER GUESSING GAME!")
    print("I'm thinking of a number between 1 and 100")
    number=randint(1,100)
    turns=difficulty()  
    guess=0
    while guess != number:
        print(f'you have {turns} attempts remaining')
        guess=int(input("make a guess:"))
    
        
        def check_answer(guess,number,turns):
            """checks answer against guess. returns the number of turns remaining"""
            if guess> number:
                print("too high")
                return turns-1
            elif guess<number:
                print("too low")
                return turns-1
            else:
                print(f'you got the right answer! it is {number}')
            
        turns=check_answer(guess,number,turns)
        if turns==0:
            print('you are out of chances.YOU LOSE!')
            return
game()





    
       
