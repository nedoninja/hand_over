import cv2
import os

class came:
    def __init__(self):
        pass

    def proverka_cm(self):
        is_working = True
        camera = cv2.VideoCapture(0)
        if not camera.isOpened():
            is_working = False

        return is_working

