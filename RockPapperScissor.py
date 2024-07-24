import random
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

def Exit():
    print(f"\nYou gained {p} points and computer gained {c} points\n")
    if p>c:
        print("Congrats!, You won\n")
    elif p<c:
        print("Sorry!, Computer won this time\n")
    else:
        print("Game is Draw\n")
    print(f"Game over!!,Thank you for playing 👼")
    exit()

c,p=0,0
while(True):
    game_images=[rock, paper, scissors]
    user_input=input("\nWhat do you choose? \nType:\n0 for Rock\n1 for Paper\n2 for Scissors\n(e or E) for Exit or to stop the game:\n")
    if user_input=='e' or user_input=='E':
        Exit()
    user_choice=int(user_input)
    print("You'r choice:\n")
    if user_choice>=3 or user_choice<0:
        print("you typed a wrong number, try again\n")
    else:
        print(game_images[user_choice])
    computer_choice = random.randint(0,2)
    print("Computer chose:")
    print(game_images[computer_choice])
    if user_choice==0 and computer_choice==2:
        print("You win!")
        p+=1
    elif computer_choice==0 and user_choice==2:
        print("You lose")
        c+=1
    elif computer_choice>user_choice:
        print("You lose")
        c+=1
    elif user_choice>computer_choice:
        print("You win!")
        p+=1
    elif computer_choice==user_choice:
        print("It's a draw")