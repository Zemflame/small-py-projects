gameLength = 6
wordLength = 5
turn = 0
message = ''
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

marking = []
for m in range(gameLength):
    marking.append([0]*wordLength)


def evaluate(index):
    if imp[index] == correctWord[index]:
        return 2

    elif imp[index] in correctWord:
        return 1

    else: 
        return 0

def applyKBV(i,index):
    global yellowLetters
    global greenLetters
    global greyLetters
    if i==1:
        yellowLetters.add(imp[index])
    if i==2:
        greenLetters.add(imp[index])
    if i==0:
        greyLetters.add(imp[index])


def printEmpty(spacing,message):
    print(' '*spacing,'[ ]'*wordLength,sep='')

def printImpHistory(spacing,message,index):
    print(' '*spacing,end='')
    for m in range(wordLength):
        if marking[index][m]==1:
            print('\033[93m','(',impHistory[index][m],')','\033[0m',sep='',end='')
        elif marking[index][m]==2:
            print('\033[92m','{',impHistory[index][m],'}','\033[0m',sep='',end='')
        else:
            print('[',impHistory[index][m],']',sep='',end='')
    print(message)
    
def printKeyboard(spacing):
    for x in keyboard:
        if x[0:1]=="\n": print('\n',' '*(spacing),x[1:],sep='',end='')
        elif x in greenLetters: print('\033[92m',x,'\033[0m',sep='',end=' ')
        elif x in yellowLetters: print('\033[93m',x,'\033[0m',sep='',end=' ')
        elif x in greyLetters: print('\033[90m',x,'\033[0m',sep='',end=' ')
        else: print(x,end=' ')
    print()


def printBoard(message):
    print('\n'*10)

    for x in range(len(impHistory)):
        printImpHistory(0,message,x)
    x=0

    for x in range(gameLength - len(impHistory)):
        printEmpty(0,message)

    printKeyboard(0)
    print('[debug]', turn, impHistory, len(impHistory),marking,sep='\n')



def getInput():
    global imp
    imp = input()
    imp = imp.lower().strip()
    if imp.isalpha():
        if len(imp) == wordLength:
            return(imp)
        else:
            message = 'wrong length'
            printBoard(message)
            getInput()
    else:
        message = 'not alpha'
        printBoard(message)
        getInput()


def mark():
    a = 0
    n = 0
    b = 0
    jint=[]
    submit=marking
    for n in range(wordLength):
        if imp.count(imp[n]):
            submit[turn][n] = evaluate(n)
            applyKBV(submit[turn][n],n)
        else:
            for a in range(wordLength):
                if imp[a] == imp[n]:
                    jint.append(evaluate(imp[a],a))
                else:
                    jint.append(0)
            a = 0
            b = 0
            while a < correctWord.count(imp[n]):
                if jint[b] == 2:
                    submit[turn][b] = 2
                    applyKBV(2,n)
                    a = a+1
                b=b+1
                if b > (wordLength-1):
                    break
            b = 0
            while a < correctWord.count(imp[n]):
                if jint[b] == 1:
                    submit[turn][b] = 1
                    applyKBV(1,n)
                    a = a+1
                b=b+1
                if b > (wordLength-1):
                    break
        jint.clear()
    return(submit)

      
printBoard(message)
while len(impHistory) < gameLength:

    impHistory.append(getInput())

    marking = mark()

    printBoard(message)
