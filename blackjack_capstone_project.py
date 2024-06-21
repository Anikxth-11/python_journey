import os
import random

def deal_Card():
    cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
    card = random.choice(cards)
    return card
def calculate_score(cards):
    """take a list of cards and returns the score calculated from the cards"""
    if sum(cards)==21 and len(cards)==2:
        return 0
    if 11 in cards and sum(cards)>21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)
def compare(user_score,computer_Score):
    if user_score==computer_Score:
        return "DRAW!"
    elif user_score==0:
        return "YOU WIN! YOU HAD A BLACKJACK!"
    elif computer_Score==0:
        return "LOSE! OPPONENT HAD A BLACKJACK!"
    elif user_score>21:
        return "YOU LOSE! YOU WENT OVER 21!"
    elif computer_Score>21:
        return "YOU WIN! OPPONENT WENT OVER 21!"
    elif user_score>computer_Score:
        return "YOU WIN!"
    else:
        return "YOU LOSE!"

def play_game():
    user_card=[]
    computer_card=[]
    for _ in range(2):
        user_card.append(deal_Card())
        computer_card.append(deal_Card())
    is_game_over=False
    while not is_game_over:
        user_score = calculate_score(user_card)
        computer_score =calculate_score(computer_card)
        print(f"your card:{user_card},current score:{user_score}")
        print(f"computer's first card:{computer_card[0]}")
        if user_score==0 or computer_score==0 or user_score>21:
            is_game_over=True
        else:
            user_should_deal= input("type 'y' to get another card and 'n' to pass:\n")
            if user_should_deal=="y":
                user_card.append(deal_Card())
            else:
                is_game_over=True
    while computer_score!=0 and computer_score<17:
        computer_card.append(deal_Card())
        computer_score=calculate_score(computer_card)
    print(f"your final hand is {user_card}, final score is:{user_score}")
    print(f"the computer's final hand is {computer_card} and its score is:{computer_score}")
    print(compare(user_score , computer_score))
while input('do you want to play a game of blackjack, type "yes" or "no":\n') == "yes":
    clear = lambda: os.system('cls')
    clear()
    play_game()

