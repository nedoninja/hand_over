import urllib.request

class server:
    def __init__(self):
        pass

    def proverka_inet(self):
        try:
            urllib.request.urlopen('http://google.com')
            return True
        except:
            return False