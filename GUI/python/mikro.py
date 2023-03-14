import speech_recognition

class mikro:
    def __init__(self):
        pass

    def proverka_mk(self):
        a = speech_recognition.Microphone.list_microphone_names()
        if "Input" in a[0]:
            return True
        elif "Output" in a[0]:
            return False