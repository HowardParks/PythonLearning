class CodeMachine:
    def __init__(self,key):
        self.key = key

    def cypher(self, text):
        result = ''
        min = 256
        max = 0
        for i in range(len(text)):
            xor = ord(text[i]) ^ ord(self.key[i % len(self.key)])
            if xor <= min:
                min = xor
            if xor >= max:
                max = xor
            result += chr(xor)
        #print(min,max)
        return result
