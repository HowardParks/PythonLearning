import random
rings = [(['S', 'R', 'Q', 'U', 'H', 'T', 'D', 'M', 'F', 'W', 'I', 'V', 'X', 'N', 'O', 'J', 'E', 'K', 'Y', 'C', 'A', 'P', 'Z', 'L', 'G', 'B'], ['Z', 'J', 'C', 'V', 'U', 'S', 'X', 'P', 'Y', 'A', 'H', 'R', 'K', 'B', 'M', 'O', 'G', 'N', 'W', 'T', 'L', 'E', 'D', 'F', 'Q', 'I'], 3), (['Q', 'H', 'T', 'B', 'D', 'F', 'S', 'P', 'W', 'K', 'I', 'V', 'R', 'L', 'O', 'G', 'C', 'N', 'U', 'Z', 'M', 'Y', 'E', 'J', 'A', 'X'], ['A', 'K', 'P', 'W', 'E', 'D', 'Q', 'I', 'V', 'Z', 'M', 'Y', 'S', 'G', 'N', 'H', 'C', 'R', 'B', 'U', 'F', 'X', 'L', 'O', 'J', 'T'], 15), (['H', 'E', 'P', 'T', 'I', 'V', 'J', 'C', 'L', 'O', 'Q', 'M', 'G', 'X', 'Z', 'B', 'D', 'W', 'R', 'K', 'F', 'U', 'S', 'N', 'Y', 'A'], ['M', 'I', 'V', 'G', 'T', 'O', 'R', 'X', 'C', 'Y', 'F', 'S', 'W', 'J', 'L', 'K', 'P', 'B', 'Z', 'A', 'D', 'Q', 'U', 'E', 'H', 'N'], 7), (['S', 'Y', 'T', 'I', 'C', 'G', 'R', 'A', 'J', 'P', 'K', 'O', 'M', 'X', 'E', 'Q', 'N', 'Z', 'V', 'H', 'U', 'F', 'W', 'L', 'D', 'B'], ['C', 'I', 'P', 'V', 'F', 'G', 'J', 'O', 'L', 'S', 'X', 'U', 'Y', 'A', 'R', 'N', 'B', 'D', 'Q', 'Z', 'W', 'K', 'H', 'E', 'M', 'T'], 23), (['S', 'N', 'X', 'M', 'K', 'E', 'D', 'J', 'O', 'V', 'H', 'P', 'U', 'A', 'T', 'C', 'F', 'R', 'B', 'Y', 'I', 'Q', 'G', 'W', 'L', 'Z'], ['U', 'M', 'O', 'F', 'C', 'Q', 'V', 'K', 'W', 'R', 'G', 'X', 'J', 'H', 'D', 'B', 'Z', 'T', 'N', 'S', 'A', 'I', 'L', 'P', 'Y', 'E'], 0), (['N', 'V', 'O', 'Y', 'E', 'C', 'K', 'G', 'R', 'U', 'F', 'H', 'J', 'L', 'M', 'X', 'Q', 'W', 'Z', 'D', 'A', 'I', 'B', 'T', 'S', 'P'], ['S', 'H', 'D', 'N', 'Z', 'A', 'R', 'E', 'Q', 'C', 'V', 'U', 'M', 'G', 'T', 'P', 'J', 'L', 'Y', 'X', 'I', 'F', 'O', 'W', 'K', 'B'], 0)]

# import string
# import random
# alpha = string.ascii_uppercase
# letters = list(alpha)
# rings=[]
# for i in range(6): # 6 is arbitrary
#     leftside = letters.copy()
#     rightside = letters.copy()
#     random.shuffle(leftside)
#     random.shuffle(rightside)
#     ringturn = random.randint(0,25)
#     rings.append((leftside,rightside,ringturn))

class Enigma:
    def __init__(self,ringlist,patchestable,startpositions):
        self.rings = ringlist
        self.patches = patchestable
        self.positions = startpositions

    def crypt(self,letter):
        # when do we use letter and when do we use position?
        # i think we use letter on the input side of the first ring and position thereafter
        # leftside - rightside show C to M means the electricity goes out at relative position 12
        # input = 'J' relative position 15, rightside = 20
        # absolute position = relative + start
        # and enters the next ring there at that absolute position.
        # so if the ring is in position 7, it goes out absolute position 19
        # if the next ring is at position 20, it enters at 20 + 19 % 25 = 14
        # we use leftside rightside

e = Enigma(1,3,4)
print(e.crypt('Hello World',2))
