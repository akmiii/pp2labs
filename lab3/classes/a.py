class String:
    def __init__(self, word):
        self.word = word
    
    def printString(self):
        print(self.word.upper())

s = String(input())
s.printString()