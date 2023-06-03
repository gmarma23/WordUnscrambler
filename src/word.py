class Word():
    # Coefficient related to max possible number of ocurrences of individual chars in words. 
    # Used in mapping vectors to the same signature-integers for permutations of same 
    # char list and ensure unique signature-integers for different char lists.
    __PARTITION_COEF = 4


    def __init__(self, charlist: str, valid_chars: list[str]) -> None:
        self.__valid_chars = []
        self.__charlist = ''
        self.__int_signature = 0

        self.__valid_chars = list(dict.fromkeys(valid_chars))
        self.__set_charlist(charlist)
        self.__vector = [0 for _ in self.__valid_chars]

        # Form string signature based on number of occurrences of each used char
        # Permutations of the same char string have identical signatures
        self.__charlist_to_vector()
        self.__vector_to_int()


    @property
    def int_signature(self) -> int:
        return self.__int_signature
        

    def __set_charlist(self, charlist: str) -> None:
        """Charlist setter"""

        invalid_chars = set(charlist).difference(self.__valid_chars)
        if len(invalid_chars):
            # Chars in provided charlist must be a subset of valid chars
            # to ensure proper search results from wordlist
            raise InvalidChar(str(invalid_chars), str(self.__valid_chars))

        self.__charlist = charlist
 

    def __charlist_to_vector(self) -> None:
        """Encode provided char string to vector"""

        for ch in self.__charlist:
            # Get char index in vector
            i = self.__valid_chars.index(ch)  

            # Increment number of char occurrences 
            self.__vector[i] += 1 


    def __vector_to_int(self) -> None:
        """Injective function to map distinct vector to distinct integer"""

        for i,n in enumerate(self.__vector):
            # "Partition coefficient" is used to approximate injective function's behavior 
            # and avoid collisions while maintaining smaller integer values.
            self.__int_signature += n*(2**(self.__PARTITION_COEF*i))


class InvalidChar(Exception):
    def __init__(self, invalid_chars: str, valid_chars: str) -> None:            
        super().__init__(f'Invalid char in charlist: {invalid_chars}.\nValid chars: {valid_chars}')
