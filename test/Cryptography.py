#-------------Cipher------------
class Cipher:
    def __init__(self):
        self.alphabet_size = 95
        self.legal_alphabet = []

    def encode(self, text):       #KODE
        return None            # Initialiseres i subklasser

    def decode(self, text):       #DEKODE
        return None            # Initialiseres i subklasser

    def verify(self, decodedText, encodedText): # Sjekker om teksten er riktig begge veier
        return decodedText == self.decode(encodedText) and encodedText == self.encode(decodedText)


    def generate_keys(self):
        return None            # Initialiseres i subklasser


#-------------Person--------------
class Person:

    def __init__(self, key):
        self.key = key


    def set_key(self, key):
        self.key = key

    def get_key(self):
        return self.key

    def operate_cipher(self): # Initialisere i sub-klasse
        None


#----------Subclass SENDER----------

class Sender(Person):
    def __init__(self):
        super().__init__(self)

    def operate_cipher(self):
        a = 0


#-----------Subclass RECIEVER--------

class Receiver(Person):

    def __init__(self):
        super().__init__(self)

    def operate_cipher(self):
        a = 0




#----------Subclass HACKER--------------

class Hacker(Person):

    def __init__(self):
        super().__init__(self)

    def operate_cipher(self):
        a = 0