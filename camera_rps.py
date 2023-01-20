import cv2
import time
import random
import numpy as np
from keras.models import load_model


def get_prediction(prediction):
    predicted_choice = np.argmax(prediction[0])
    categories = ["Rock", "Paper", "Scissors", "Nothing"]
    print(f"You chose {categories[predicted_choice]}")
    class_predictions = dict(zip(categories, prediction[0]))
#    print(class_predictions)
    return categories[predicted_choice]


def capture_user_choice():
    model = load_model('keras_model.h5')
    # start video
    cap = cv2.VideoCapture(0)
    data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

    countdown = 5

    while True:
        start_time = time.time()
        ret, frame = cap.read()
        # cv2.imshow('frame', frame)
        # cv2.waitKey(1)

        while countdown >= 0:
            ret, frame = cap.read()
            cv2.imshow('frame', frame)
            cv2.waitKey(1)
            time_now = time.time()

            if time_now - start_time >= 1:
                countdown = (countdown - int(time_now - start_time))
                start_time = time_now
            print(countdown)

        else:
            ret, frame = cap.read()
            cv2.imshow('frame', frame)
            resized_frame = cv2.resize(frame, (224, 224), interpolation = cv2.INTER_AREA)
            image_np = np.array(resized_frame)
            normalized_image = (image_np.astype(np.float32) / 127.0) - 1 # Normalize the image
            data[0] = normalized_image
            prediction = model.predict(data)
        #     # Press q to close the window
            print(prediction)
            cv2.waitKey(5000)
            break

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
                
    # After the loop release the cap object
    cap.release()
    # Destroy all the windows
    cv2.destroyAllWindows()
    user_choice = get_prediction(prediction)
    return user_choice

def get_computer_choice():
    return random.choice(["Rock", "Paper", "Scissors"])


def get_user_choice():
#    prediction = capture_user_choice()
#    user_choice = capture_user_choice()
    return capture_user_choice()

def get_winner(computer_choice, user_choice):
    if computer_choice == user_choice:
            print("It is a tie!")
    elif computer_choice == "Rock":
        if user_choice == "Paper":
            print("You won!")
#            user_wins += 1
        elif user_choice == "Scissors":
            print("You lost")
#            computer_wins += 1
    elif computer_choice == "Paper":
        if user_choice == "Scissors":
            print("You won!")
#            user_wins += 1
        elif user_choice == "Rock":
            print("You lost")
#            computer_wins += 1            
    else:
        if user_choice == "Rock":
            print("You won!")
#            user_wins += 1
        elif user_choice == "Paper":
            print("You lost")
#            computer_wins += 1    


def play():
    rounds_played = 0
    computer_wins = 0
    user_wins = 0
    while rounds_played < 5 and user_wins < 3 and computer_wins < 3:
        computer_choice = get_computer_choice()
        user_choice = get_user_choice()
    #    print(f"Computer: {computer_choice} User: {user_choice}")
        winner = get_winner(computer_choice, user_choice)
        if winner =="user":
            user_wins += 1
        elif winner == "computer":
            computer_wins += 1
        rounds_played += 1


play()   