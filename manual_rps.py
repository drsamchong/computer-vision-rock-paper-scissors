import random


def get_computer_choice():
    return random.choice(["Rock", "Paper", "Scissors"])


def get_user_choice():
    return input('Please choose "Rock", "Paper" or "Scissors"\n')


def get_winner(computer_choice, user_choice):
    if computer_choice == user_choice:
            print("It's a tie!")
    elif computer_choice == "Rock":
        if user_choice == "Paper":
            print("You won!")
#            user_wins += 1
        elif user_choice == "Scissors":
            print("You lost!")
#            computer_wins += 1
    elif computer_choice == "Paper":
        if user_choice == "Scissors":
            print("You won!")
#            user_wins += 1
        elif user_choice == "Rock":
            print("You lost!")
#            computer_wins += 1            
    else:
        if user_choice == "Rock":
            print("You won!")
#            user_wins += 1
        elif user_choice == "Paper":
            print("You lost!")
#            computer_wins += 1    


def play():
    computer_choice = get_computer_choice()
    user_choice = get_user_choice()
    print(f"Computer: {computer_choice} User: {user_choice}")
    get_winner(computer_choice, user_choice)


play()    