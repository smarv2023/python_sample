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

# Write your code below this line 👇

import random

choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors\n"))
if choice > 2:
    print("Invalid choice, you lose!")
else:
    game_images = [rock, paper, scissors]
    print(game_images[choice])

    print("Computer chose")

    random_num = random.randint(0, 2)
    print(game_images[random_num])

    if choice > random_num:
        if choice == 2 and random_num == 0:
            print("You lost")
        else:
            print("You won")
    elif choice < random_num:
        if choice == 0 and random_num == 2:
            print("You won")
        else:
            print("You lost")
    elif choice == random_num:
        print("It's a draw!")
