# i cant be bothered with comments 
# just know i didnt use chatgpt and this code is way better
# like 20x better
import random
gameLength = 6
wordLength = 5
wordChecking = True
customWords = False
turn = 0
message = 'made by @zemflame'
imp = ''
impHistory = []
greyLetters = set()
yellowLetters = set()
greenLetters = set()
correctWord = ['A','B','A','T','E']
keyboard = [
    '\n','Q','W','E','R','T','Y','U','I','O','P',
    '\n ','A','S','D','F','G','H','J','K','L',
    '\n   ','Z','X','C','V','B','N','M']
keyboardWidth = max( (len((''.join(keyboard[1:])).split('\n')[0])*2),(len((''.join(keyboard[2:])).split('\n')[0])*2),(len((''.join(keyboard[3:])).split('\n')[0])*2),)-1
marking = []
for m in range(gameLength):
    marking.append([0]*wordLength)
boardOffset = int((abs((wordLength*3)-keyboardWidth)+(keyboardWidth-(wordLength*3)))/4)
keyboardOffset = int((abs((wordLength*3)-keyboardWidth)+((wordLength*3)-keyboardWidth))/4)


def scanList(target):
    for a in content:
        if a[:5] == target:
            return(True)
    return(False)

def evaluate(index):
    if imp[index] == correctWord[index]:
        return 2

    elif imp[index] in correctWord:
        return 1

    else: 
        return 0

def applyKBV(i,index):
    if i==1:
        yellowLetters.add(imp[index])
    if i==2:
        greenLetters.add(imp[index])
    if i==0:
        greyLetters.add(imp[index])

def printEmpty(message):
    print(' '*boardOffset,'[ ]'*wordLength,' '*(boardOffset+2),message,sep='')

def printImpHistory(message,index):
    print(' '*boardOffset,end='')
    for m in range(wordLength):
        if marking[index][m]==1:
            print('\033[93m','(',impHistory[index][m],')','\033[0m',sep='',end='')
        elif marking[index][m]==2:
            print('\033[92m','{',impHistory[index][m],'}','\033[0m',sep='',end='')
        else:
            print('[',impHistory[index][m],']',sep='',end='')
    print(' '*(boardOffset+1),message)
    
def printKeyboard():
    for x in keyboard:
        if x[0:1]=="\n": print('\n',' '*(keyboardOffset),x[1:],sep='',end='')
        elif x in greenLetters: print('\033[92m',x,'\033[0m',sep='',end=' ')
        elif x in yellowLetters: print('\033[93m',x,'\033[0m',sep='',end=' ')
        elif x in greyLetters: print('\033[90m',x,'\033[0m',sep='',end=' ')
        else: print(x,end=' ')
    print()

def printBoard(message):
    print('\n'*20)

    for x in range(len(impHistory)):
        printImpHistory(message,x)
    x=0

    for x in range(gameLength - len(impHistory)):
        printEmpty(message)

    printKeyboard()

def getInput():
    imp = input(' >')
    imp = imp.upper().strip()
    if imp.isalpha():
        if len(imp) == wordLength:
            if wordChecking == True:
                if scanList(imp.lower()):
                    return(imp)
                else:
                    message = 'word not found'
                    printBoard(message)
                    return getInput()
            else:
                return(imp)
        else:
            message = 'wrong length'
            printBoard(message)
            return getInput()
    else:
        message = 'invalid characters'
        printBoard(message)
        return getInput()

def mark():
    a = 0
    n = 0
    b = 0
    jint=[]
    submit=marking
    for n in range(wordLength):
        if imp.count(imp[n])<2:
            submit[turn][n] = evaluate(n)
            applyKBV(submit[turn][n],n)
        else:
            for a in range(wordLength):
                if imp[a] == imp[n]:
                    jint.append(evaluate(a))
                else:
                    jint.append(0)
            a = 0
            b = 0
            while a < correctWord.count(imp[n]):
                if jint[b] == 2:
                    submit[turn][b] = 2
                    applyKBV(2,n)
                    a=a+1
                b=b+1
                if b > (wordLength-1):
                    break
            b = 0
            while a < correctWord.count(imp[n]):
                if jint[b] == 1:
                    submit[turn][b] = 1
                    applyKBV(1,n)
                    a=a+1
                b=b+1
                if b > (wordLength-1):
                    break
        jint.clear()
    return(submit)

if customWords == True:
    printBoard('enter custom answer')
    correctWord = list(input(' >').upper().strip())
    for _ in range(wordLength-len(correctWord)):
        correctWord.append(correctWord[-1])
else:
    if wordLength == 5:
        with open("potentialAnswers", "rt") as s:
            content = s.readlines()
            correctWord = list(content[random.randint(0,2314)].upper())[0:5]
    else:
        printBoard('autoword is only for 5 letter words. enter custom answer')
        correctWord = list(input(' >').upper().strip())
        for _ in range(wordLength-len(correctWord)):
            correctWord.append(correctWord[-1])

with open ("allowedWords", "rt") as s:
    content = s.readlines()

printBoard(message)
while turn < gameLength:
    imp = getInput()
    impHistory.append(imp)
    marking = mark()
    if marking[turn] == [2]*wordLength:
        printBoard('you win')
        exit()
    turn=turn+1
    printBoard(message)
printBoard('you lose, word was:',''.join(correctWord).lower())
