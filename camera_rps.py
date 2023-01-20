import cv2
import time
from keras.models import load_model
import numpy as np

def get_prediction(prediction):
    predicted_choice = np.argmax(prediction[0])
    categories = ["Rock", "Paper", "Scissors", "Nothing"]
    print(f"You chose {categories[predicted_choice]}")
    class_predictions = dict(zip(categories, prediction[0]))
#    print(class_predictions)
    return class_predictions


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


predicted_classes = get_prediction(prediction)

