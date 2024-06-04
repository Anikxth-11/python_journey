print('WELCOME TO TREASURE ISLAND!!\n\n')
print('YOU ARE ON A MISSION TO FIND THE TREASURE!')

road = input('You are at a cross-road. Where do you want to go? To the left or right?\n')
if road.lower() == 'left':
    lake = input("You arrived at a lake. There is an island in the middle of the lake. Type 'swim' to swim and 'wait' to wait for the boat.\n")
    if lake.lower() == 'wait':
        island = input("You arrived at the island unharmed. There are three doors to go into the cave. Which door would you like to go in? Type 'yellow' or 'red' or 'blue'.\n")
        if island.lower() == 'yellow':
            print('CONGRATULATIONS! YOU FOUND THE TREASURE!')
        elif island.lower() == 'red':
            print("GAME OVER! YOU FOUND YOUR FUTURE WIFE.")
        elif island.lower() == 'blue':
            print("GAME OVER! YOU WERE EATEN BY A HUNGRY CHEETAH.")
        else:
            print("GAME OVER! Invalid choice. Please start again.")
    elif lake.lower() == 'swim':
        print("GAME OVER! YOU WERE SWALLOWED BY PIRANHAS.")
    else:
        print("GAME OVER! Invalid choice. Please start again.")
elif road.lower() == 'right':
    print("GAME OVER! YOU REACHED A DEVIL'S DEN.")
else:
    print("GAME OVER! Invalid choice. Please start again.")
