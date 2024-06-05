names=names_string.split(", ")
import random
length=len(names)
random_choice=random.randint(0,length-1)
print(f'{names[random_choice]} is going to buy the meal today!')
