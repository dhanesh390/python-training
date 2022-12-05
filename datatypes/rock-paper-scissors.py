import random
from constants import myconstants

# game_attributes = ('rock', 'paper', 'scissors')

game_completed = myconstants.FALSE

while not game_completed:
    user_choice = int(input('What do you choose? Type 0 for rock, 1 for paper or 2 for scissors.\n'))
    print(myconstants.GAME_ATTRIBUTES[user_choice])
    # print(game_attributes[user_choice])

    computer_choice = random.randint(0, 2)
    print('computer chose: ')
    print(myconstants.GAME_ATTRIBUTES[computer_choice])
    # print(game_attributes[computer_choice])

    if user_choice >= 3 or user_choice < 0:
        print('Invalid choice , you lose!')
    elif user_choice == 0 and computer_choice == 2:
        print('you win')
    elif computer_choice == 0 and user_choice == 2:
        print('You lose')
    elif computer_choice > user_choice:
        print('You lose')
    elif user_choice > computer_choice:
        print('You win')
    elif computer_choice == user_choice:
        print("It's a draw")

    should_continue = input('Do you want to play again. Type "Yes or no": ')
    if should_continue == myconstants.YES:
        game_completed = myconstants.FALSE
    elif should_continue == myconstants.NO:
        game_completed = myconstants.TRUE
