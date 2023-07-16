import random as rm

rock = '''
    __
---'   )
      ()
      ()
      ()
---.()
'''

paper = '''
    __
---'   )
        ___)
          __)
         __)
---.__)
'''

scissors = '''
    __
---'   )
          __)
          __)
    (__)
---.(___)
'''
game_images = [rock,paper,scissors]

x = 0
y = 1
z = 2

user_choice = int(input(f"What do you choose.Type {x} to choose rock,Type {y} for paper or type {z} for scissors.\n"))
print(game_images[user_choice])

computer_choice = rm.randint(0, 2)
print("Computer choice: ")
print(game_images[computer_choice])

if user_choice == 3 or user_choice >= 3:
    print("You're Out")

if user_choice == 0 and computer_choice == 0:
    print("█▀▄ █▀█ ▄▀█ █░█░█\n█▄▀ █▀▄ █▀█ ▀▄▀▄▀")
if user_choice == 0 and computer_choice == 1:
    print("█▄█ █▀█ █░█   █░░ █▀█ █▀ █▀▀\n░█░ █▄█ █▄█   █▄▄ █▄█ ▄█ ██▄")
if user_choice == 0 and computer_choice == 2:
    print("█▄█ █▀█ █░█   █░█░█ █▀█ █▄░█\n░█░ █▄█ █▄█   ▀▄▀▄▀ █▄█ █░▀█")


if user_choice == 1 and computer_choice == 0:
    print("█▄█ █▀█ █░█   █░█░█ █▀█ █▄░█\n░█░ █▄█ █▄█   ▀▄▀▄▀ █▄█ █░▀█")
if user_choice == 1 and computer_choice == 1:
    print("█▀▄ █▀█ ▄▀█ █░█░█\n█▄▀ █▀▄ █▀█ ▀▄▀▄▀")
if user_choice == 1 and computer_choice == 2:
    print("█▄█ █▀█ █░█   █░░ █▀█ █▀ █▀▀\n░█░ █▄█ █▄█   █▄▄ █▄█ ▄█ ██▄")


if user_choice == 2 and computer_choice == 0:
    print("█▄█ █▀█ █░█   █░░ █▀█ █▀ █▀▀\n░█░ █▄█ █▄█   █▄▄ █▄█ ▄█ ██▄")
if user_choice == 2 and computer_choice == 1:
    print("█▄█ █▀█ █░█   █░█░█ █▀█ █▄░█\n░█░ █▄█ █▄█   ▀▄▀▄▀ █▄█ █░▀█")
if user_choice == 2 and computer_choice == 2:
    print("█▀▄ █▀█ ▄▀█ █░█░█\n█▄▀ █▀▄ █▀█ ▀▄▀▄▀")