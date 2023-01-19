import random


def get_computer_choice():
    return random.choice(["Rock", "Paper", "Scissors"])


def get_user_choice():
    return input('Please choose "Rock", "Paper" or "Scissors"')


def get_winner(computer_choice, user_choice):
    if computer_choice == "Rock":
        if user_choice == "Paper":
            print("You won!")
            user_wins += 1
        elif user_choice == "Scissors":
            print("You lost!")
            computer_wins += 1
        else:
            print("It's a tie")

    elif computer_choice == "Paper":
        if user_choice == "Scissors":
            print("You won!")
            user_wins += 1
        elif user_choice == "Rock":
            print("You lost!")
            computer_wins += 1
        else:
            print("It's a tie")
            
    elif computer_choice == "Scissors":
        if user_choice == "Rock":
            print("You won!")
            user_wins += 1
        elif user_choice == "Paper":
            print("You lost!")
            computer_wins += 1    
        else:
            print("It's a tie")
