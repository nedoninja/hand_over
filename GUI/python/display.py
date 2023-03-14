from screeninfo import get_monitors

class display:
    def __init__(self):
        pass

    def proverka_dsp(self):
        k = 0 
        for _ in get_monitors():
            k+=1
        # if k > 1:
        #     return False
        # elif k == 1:
        #     return True
        return True