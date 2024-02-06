"""
Takes in images from the pi camera
then classifies them using a pre-trained model
if the image is classified as an authorized person
then it will open the door
"""

import time
import numpy as np
from picamera import PiCamera
from picamera.array import PiRGBArray
from keras.preprocessing import image
from keras.preprocessing.image import img_to_array
from keras.applications.mobilenet import preprocess_input
from keras.applications.mobilenet import decode_predictions
from keras.models import load_model


class ImageClassifier:
    def __init__(self, model_path, door_opener):
        self.model = load_model(model_path)
        self.door_opener = door_opener

    def classify_image(self, img):
        img = img.resize((224, 224))
        img = img_to_array(img)
        img = np.expand_dims(img, axis=0)
        img = preprocess_input(img)
        prediction = self.model.predict(img)
        prediction = decode_predictions(prediction)
        return prediction

    def run(self):
        camera = PiCamera()
        camera.resolution = (640, 480)
        camera.framerate = 32
        rawCapture = PiRGBArray(camera, size=(640, 480))

        time.sleep(0.1)

        for frame in camera.capture_continuous(
            rawCapture, format="bgr", use_video_port=True
        ):
            img = frame.array
            img = image.array_to_img(img)
            prediction = self.classify_image(img)
            print(prediction)
            prediction = np.argmax(prediction, axis=1)
            if prediction[0] == 1:
                print("Authorized")
                # self.door_opener.open_door()
                # self.door_opener.close_door()
            else:
                print("Unauthorized")
            rawCapture.truncate(0)
