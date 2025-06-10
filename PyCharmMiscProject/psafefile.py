from codemachine import CodeMachine
import json
# Trying with utf-8, psafeb.fil is still intact at 16
SAFE="C://Users/Owner/Downloads/psafeb8.fil"

class PsafeFile:
    def __init__(self, key):
        self.codeMachine = CodeMachine(key)

    def read(self):
        with open(SAFE, "rb") as infile:
            cba = infile.read()
        crypted = cba.decode('utf-8')  # trying with 8
        psafe = {}
        js = self.codeMachine.cypher(crypted)
        psafe = json.loads(js)
        return psafe

    def write(self, psafe):
        js = json.dumps(psafe)
        crypted = self.codeMachine.cypher(js)
        oba = bytearray(crypted, 'utf-8')  # trying with 8
        with open(SAFE, 'wb') as outfile:
            outfile.write(oba)
