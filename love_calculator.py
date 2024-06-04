
name1 = input("enter the first person's name:\n") 
name2 = input("enter the second person's name:\n") 
combined_name= name1+name2
lower_names=combined_name.lower()
t=lower_names.count('t')
r=lower_names.count('r')
u=lower_names.count('u')
e=lower_names.count('e')
first_digit = t+r+u+e 

l=lower_names.count('l')
o=lower_names.count('o')
v=lower_names.count('v')
e=lower_names.count('e')
second_digit = l+o+v+e
print("The Love Calculator is calculating your score...")

score=int(str(first_digit)+str(second_digit))

if (score<10) or (score>90):
  print(f'Your score is {score}, you go together like coke and mentos.')

elif (score>=40) and (score<=50):
  print(f'Your score is {score}, you are alright together.')
else:
  print(f'Your score is {score}.')
  
