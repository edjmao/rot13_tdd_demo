
class ROT13(object):

    def __init__(self, plaintext=""):
        self.plaintext = plaintext

    def __str__(self):
        
        return "".join([self._getCipherText(c) for c in self.plaintext])

    def _getCipherText(self, char):
        ordinal = ord(char)
        if (ordinal >= ord('A') and ordinal <= ord('Z')) \
           or (ordinal >= ord('a') and ordinal <= ord('z')):
            
            if (ordinal >= ord('N') and ordinal <= ord('Z')) \
               or (ordinal >= ord('n') and ordinal <= ord('z')):
                ordinal -= 26
            return chr(ordinal + 13)
        return char
