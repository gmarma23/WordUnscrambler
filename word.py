
class Word():
    DEFAULT_VALID_CHARS = [chr(n) for n in range(97, 123)] + ['-']

    def __init__(self, charlist, valid_chars=None):
        self.__valid_chars = ''
        self.__charlist = ''
        self.__int_signature = 0
        self.__set_valid_chars(valid_chars)
        self.__set_charlist(charlist)
        self.__vector = [0 for _ in self.__valid_chars]
        
    def __set_valid_chars(self, valid_chars):
        if not valid_chars:
            self.__valid_chars = self.DEFAULT_VALID_CHARS
        else:
            if len(valid_chars):    
                self.__valid_chars = list(set(valid_chars))
            else:
                raise EmptyValidCharlist()

    def __set_charlist(self, charlist):
        if set(charlist).issubset(self.__valid_chars):
            self.__charlist = charlist
        else:
            raise InvalidChar()

    def __charlist_to_vector(self):
        for ch in self.__charlist:
            i = self.__valid_chars.index(ch)
            self.__vector[i] += 1

    def __vector_to_int(self):
        for i,n in enumerate(self.__vector):
            print(self.__int_signature)
            self.__int_signature += n*(2**(4*i))

    def get_int_signature(self):
        self.__charlist_to_vector()
        self.__vector_to_int()
        return self.__int_signature


class InvalidChar(Exception):
    def __init__(self):            
        super().__init__('Invalid char in charlist')


class EmptyValidCharlist(Exception):
    def __init__(self):            
        super().__init__('Provided valid char list is empty')
