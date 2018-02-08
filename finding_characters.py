word_list = ['hello','world','my','name','is','Anna']
char = 'a'

def findCharacter (varList, character):
    for val in varList:
        for element in val:
            if element == character:
                print val + " "

findCharacter(word_list, char)