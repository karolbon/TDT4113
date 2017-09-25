import math
#-------------
def modular_inverse(a, m):
    """
    Return the value x so that a*x = 1 (mod m) -- that is, so that a*x = k*m + 1 for some non-negative integer k.
    :param a: Value of a -- positive integer. This is the encoding key in the crypto-setting
    :param m: Value of m -- positive integer This is the length of the alphabet in the crypto-setting
    :return: Solution x -- positive integer.
    # """

    def extended_gcd(_a, _b):
        """ Use the Extended Euclidean algorithm to calculate the "extended greatest common divisor".
        It takes as input two positive integers a and b, then calculates the following:
        1. The greatest common divisor (gcd) between a and b -- that is, the integer number g which is the largest
            integer for which a/g and b/g both are integers  (This can also be obtained using math.gcd)
        2. The integer x and y so that a*x + b*y = gcd(x, y)
        :param _a: Positive integer
        :param _b: Positive integer
        :return: Tuple (gcd, x, y)
        """
        previous_remainder, remainder = _a, _b
        current_x, previous_x, current_y, previous_y = 0, 1, 1, 0
        while remainder > 0:
            previous_remainder, (quotient, remainder) = remainder, divmod(previous_remainder, remainder)
            current_x, previous_x = previous_x - quotient * current_x, current_x
            current_y, previous_y = previous_y - quotient * current_y, current_y
        # The loop terminates with remainder == 0, x == b and y == -a. This is not what we want, and is because we have
        # walked it through one time "too many". Therefore, return the values of the previous round:
        return previous_remainder, previous_x, previous_y

    gcd_value, x, y = extended_gcd(a, m)
    if gcd_value != 1:
        print('No inverse. gcd (%d, %d) is %d. Decoding is not unique. Choose another key than %d'
              % (a, m, math.gcd(a, m), a))
    return x % m


#-------------Cipher------------
class Cipher:
    def __init__(self):
        #self.alphabet_size = 95
        #self.legal_alphabet = " !\"#$%&\'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~"

        self.legal_alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        self.alphabet_size = 26

    def encode(self, text):       #KODE
        return None            # Initialiseres i subklasser

    def decode(self, text):       #DEKODE
        return None            # Initialiseres i subklasser

    def verify(self, decodedText, encodedText): # Sjekker om teksten er riktig begge veier
        return decodedText == self.decode(encodedText) and encodedText == self.encode(decodedText)


    def generate_keys(self):
        return None            # Initialiseres i subklasser





#-----------Subclass_Caesar----------
class Caesar(Cipher):
    def __init__(self, secret_key):
        super().__init__()
        self.secret_key  = secret_key


    def encode(self, text): # Gjøre om original tekst til kodet tekst/kryptere
        self.encoded_text = ""

        for symbol in text:
            index_in_alphabet = self.legal_alphabet.index(symbol)
            self.encoded_text += self.legal_alphabet[(index_in_alphabet+self.secret_key)%self.alphabet_size]

        return self.encoded_text

    def decode(self, text):
        self.decoded_text = ""

        for symbol in text:
            index_in_alphabet = self.legal_alphabet.index(symbol)
            self.decoded_text += self.legal_alphabet[(index_in_alphabet-self.secret_key)%self.alphabet_size]

        return self.decoded_text

    def generate_keys(self):
        return [self.secret_key, self.alphabet_size-self.secret_key]


class Mult_Cipher(Cipher):

    def __init__(self, secret_key):
        super().__init__()
        self.secret_key = secret_key

    def encode(self, text):
        self.encoded_text = ""
        for symbol in text:
            index_in_alphabet = self.legal_alphabet.index(symbol)
            self.encoded_text += self.legal_alphabet[(index_in_alphabet*self.secret_key)%self.alphabet_size]

        return self.encoded_text

    def decode(self, text):
        self.decoded_text = ""
        self.secret_key_mod_inverse = modular_inverse(self.secret_key, self.alphabet_size)


        for symbol in text:
            index_in_alphabet = self.legal_alphabet.index(symbol)
            self.decoded_text += self.legal_alphabet[(index_in_alphabet*self.secret_key_mod_inverse)%self.alphabet_size]

        return self.decoded_text

    def generate_keys(self):
        a = 0

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
    def __init__(self, key):
        super().__init__(self, key)

    def operate_cipher(self):
        a = 0


#-----------Subclass RECIEVER--------

class Receiver(Person):

    def __init__(self, key):
        super().__init__(self, key)

    def operate_cipher(self):
        a = 0




#----------Subclass HACKER--------------

class Hacker(Person):

    def __init__(self):
        super().__init__(self)

    def operate_cipher(self):
        a = 0


def  main():
    caesar = Caesar(2)
    caesar1 = Caesar(24)
    print(caesar1.encode("RAVJQP"))
    print(caesar.encode("PYTHON"))
    print(caesar.decode("RAVJQP"))
    print(caesar.generate_keys())
    print(caesar.verify("KODE", caesar.encode("KODE")))

    mult = Mult_Cipher(3)
    print(mult.encode("KODE"))
    print(mult.decode("EQJM"))
    print(mult.verify("EQJM", mult.encode("EQJM")))

main()



