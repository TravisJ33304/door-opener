"""
Creates the image classifier and runs it using a pre-trained model
"""

from image_classifier import ImageClassifier
from motor_driver import MotorDriver

if __name__ == "__main__":
    model_path = "models/model.h5"
    motor_driver = MotorDriver(17, 27, 22, 10, 200, 0.01, 0.01)
    image_classifier = ImageClassifier(model_path, motor_driver)
    image_classifier.run()
