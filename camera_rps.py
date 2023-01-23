import cv2
import time
import random
import numpy as np
from keras.models import load_model


def capture_user_choice():
    model = load_model('keras_model.h5')
    # start video
    cap = cv2.VideoCapture(0)
    data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

    countdown = 3

    while True:
        start_time = time.time()
        ret, frame = cap.read()

        while countdown >= 0:
            ret, frame = cap.read()
            # crop to same aspect ratio as Teachable Machine training set
            crop = frame[:, 420:1501]
            # add countdown text to the image displayed
            font = cv2.FONT_HERSHEY_SIMPLEX
            cv2.putText(crop, str(countdown), (480, 480), font, 10, (255, 0 , 255), 4, cv2.LINE_AA)
            cv2.imshow('crop', crop)
            cv2.waitKey(10)
            time_now = time.time()

            if time_now - start_time >= 1:
                countdown = (countdown - int(time_now - start_time))
                start_time = time_now
            print(countdown)

        else:
            ret, frame = cap.read()
            crop = frame[:, 420:1501]
            resized_frame = cv2.resize(crop, (224, 224), interpolation = cv2.INTER_AREA)
            image_np = np.array(resized_frame)
            normalized_image = (image_np.astype(np.float32) / 127.0) - 1  # Normalize the image
            data[0] = normalized_image
            prediction = model.predict(data)
#            print(prediction)
            user_choice = get_prediction(prediction)
            cv2.putText(crop, str(user_choice), (280, 480), font, 5, (255, 0 , 255), 4, cv2.LINE_AA)
            cv2.imshow('crop', crop)
            cv2.waitKey(2000)
            break

        # Press q to close the window
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    if user_choice == "Nothing":
        print("No choice detected. Try again")
        user_choice = capture_user_choice()

    # After the loop release the cap object
    cap.release()
    # Destroy all the windows
    cv2.destroyAllWindows()

    return user_choice


def get_prediction(prediction):
    predicted_choice = np.argmax(prediction[0])
    categories = ["Rock", "Paper", "Scissors", "Nothing"]
    return categories[predicted_choice]


def get_computer_choice():
    return random.choice(["Rock", "Paper", "Scissors"])


def get_user_choice():
    return capture_user_choice()


def get_winner(computer_choice, user_choice):
    print(f"in get_winner: {user_choice}")
    if computer_choice == user_choice:
            print("It is a tie!")
            winner = "neither"
    elif computer_choice == "Rock":
        if user_choice == "Paper":
            print("You won!")
            winner = "user"
        elif user_choice == "Scissors":
            print("You lost")
            winner = "computer"
    elif computer_choice == "Paper":
        if user_choice == "Scissors":
            print("You won!")
            winner = "user"
        elif user_choice == "Rock":
            print("You lost")
            winner = "computer"
    else:
        if user_choice == "Rock":
            print("You won!")
            winner = "user"
        elif user_choice == "Paper":
            print("You lost")
            winner = "computer"
    return winner

def play():
    rounds_played = 0
    computer_wins = 0
    user_wins = 0
    while rounds_played < 5: # and user_wins < 3 and computer_wins < 3:
        computer_choice = get_computer_choice()
        user_choice = get_user_choice()
    #    print(f"Computer: {computer_choice} User: {user_choice}")
        winner = get_winner(computer_choice, user_choice)

        if winner =="user":
            user_wins += 1
        elif winner == "computer":
            computer_wins += 1
        rounds_played += 1
        print(f"Computer wins: {computer_wins}. User wins: {user_wins}. Rounds played: {rounds_played}")

        if computer_wins == 3:
            print("Computer wins")
            break
        elif user_wins == 3:
            print("User wins")
            break
    else:
        print("Game over!")

play()

# TODO
# OOP