class CodeMachine:
    def __init__(self,key):
        self.key = key

    def cypher(self, text):
        result = ''
        for i in range(len(text)):
            xor = ord(text[i]) ^ ord(self.key[i % len(self.key)])
            result += chr(xor)
        return result
