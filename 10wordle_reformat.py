# THIS PROJECT IS DONE

# made w/o any chatgpt whatsoever
# the marking is 100% accurate to real wordle
# it took like 4 hours to get it correct

# currently feature-complete
# but the code is really messy
# will fix if i feel like it

import random
# importandt variables
gameLength=6
wordLength=5
checkWords=True

# iterating variables
n=0
a=0
c=0
d=0
m=0
iterations=0

# lists n stuff
lineClears=20
advanceTurn=True
messageBuffer='hi twin'
jint=[]
imp='uhoh something broek'
impHistory=[]
turn=0
greyLetters=set()
yellowLetters=set()
greenLetters=set()
boardSpacing=2
# keyboard for qwerty
keyboardWidth=19
keyboard=[
    '\n','Q','W','E','R','T','Y','U','I','O','P',
    '\n ','A','S','D','F','G','H','J','K','L',
    '\n   ','Z','X','C','V','B','N','M']
# keyboard for colemak dh:
#keyboardWidth=19
#keyboard=[
#    '\n ','Q','W','F','P','B','J','L','U','Y',
#    '\n','A','R','S','T','G','M','N','E','I','O',
#    '\n   ','Z','X','C','D','V','K','H'
#]

#keyboardWidth = max( (len((''.join(keyboard[1:])).split('\n')[0])*2)-1,(len((''.join(keyboard[2:])).split('\n')[0])*2)-1,(len((''.join(keyboard[3:])).split('\n')[0])*2)-1,)

# individual letter checking
def evaluate(letter,index):
    if letter == correctWord[index]:
        return 2

    elif letter in correctWord:
        return 1

    else: 
        return 0

# stands for "apply keyboard visual"
def applyKBV(i,index):
    if i==1:
        yellowLetters.add(imp[index])
    if i==2:
        greenLetters.add(imp[index])
    if i==0:
        greyLetters.add(imp[index])

def scanList(target,THElist):
    randomAssVariable=0
    while randomAssVariable<12973:
        if THElist[randomAssVariable].strip()==target:
            return(True)
        randomAssVariable=randomAssVariable+1
    return(False)


def printKeyboard(preSpacing):
    for x in keyboard:
        if x[0:1]=="\n": print('\n',' '*(preSpacing),x[1:],sep='',end='')
        elif x in greenLetters: print('\033[92m',x,'\033[0m',sep='',end=' ')
        elif x in yellowLetters: print('\033[93m',x,'\033[0m',sep='',end=' ')
        elif x in greyLetters: print('\033[90m',x,'\033[0m',sep='',end=' ')
        else: print(x,end=' ')
    print('\n')

while True:
    print('\n'*lineClears)
    print('    -- WORDLE --\n>1| PLAY\n>2| options')
    imp=input('')
    imp=imp.lower().strip()

    if (imp=='options') or (imp=='o') or (imp=='2'):
        while True:
            print('\n'*lineClears)
            print(' - OPTIONS - \nchoose an option to change:'
            '\n>1| gameLength:',gameLength,
            '\n>2| wordLength:',wordLength,
            '\n>3| checkWords:', checkWords,
            '\n>4| BACK')

            imp=input('')
            imp=imp.lower().strip()

            if (imp=='gamelength') or (imp=='g') or (imp=='1'):
                print('\n'*lineClears)
                while True:
                    imp=input('type a value for gameLength:\n')
                    if imp.isnumeric():
                        if (int(imp)>0):
                            gameLength=int(imp)
                            break
                        else:
                            print('\n'*lineClears)
                            print('did you really just try to\nmake the game 0 rounds long bruh\ntry think how thats gonna work out')
                            continue
                    else:
                        print('\n'*lineClears)
                        print('type an integer')
                imp=''
                
            elif (imp=='wordlength') or (imp=='w') or (imp=='2'):
                print('\n'*lineClears)
                while True:

                    imp=input('type a value for wordLength:\n')
                    if imp.isnumeric():
                        if (int(imp)>0):
                            wordLength=int(imp)
                            break
                        else:
                            print('\n'*lineClears)
                            print('get back to me when you\nthink of a 0 letter word')
                            continue
                    else:
                        print('\n'*lineClears)
                        print('type an integer')
                imp=''
                
            elif (imp=='checkWords') or (imp=='c') or (imp=='3'):
                print('\n'*lineClears)
                while True:

                    imp=input('type a value for checkWords:\n')
                    imp=imp.lower().strip()
                    if imp==('true') or imp==('1') or imp==('t') or imp==('y'):
                        checkWords=True
                        break
                    elif imp==('false') or imp==('0') or imp==('f') or imp==('n'):
                        checkWords=False
                        break
                    else:
                        print('\n'*lineClears)
                        print('type either T/F or 1/0 or Y/N')
                imp=''
            else: break
        
    elif (imp=='play') or (imp=='p') or (imp=='1') or (imp==''):
        break
    else: continue



if wordLength==5:
    # getting random 5 letter word
    with open("potentialAnswers", "rt") as s:
        content = s.readlines()
        # random.randint() can have constants because i am using the offical wordlist
        # it is also much faster than checking the length of the file every time
        correctWord = list(content[random.randint(0,2314)].upper())[0:5]
        #print('[debug]',correctWord)
else:
    # ask user for word if its not 5 letters
    print('auto random word choosing\nis not supported for words\nthat arent 5 letters.\n')
    while True:
        correctWord = input('manually type your wordle solution here:\n       ')
        correctWord = list(correctWord.upper().strip())
        if len(correctWord)==wordLength and ''.join(correctWord).isalpha():
            break
        else: print('you supposed to type a',wordLength,'letter word brh')
#correctWord=['T','R','A','I','T']
#print('[debug]', correctWord)

# intro screen

# create marking[]
marking = []
for m in range(gameLength):
    marking.append([0]*wordLength)
#print('[debug] marking:',marking)
m=0

s = open("allowedWords", "rt")
content = s.readlines()


print('\n'*lineClears)


#calculate spacing

emptyWidth=wordLength*3
if emptyWidth<keyboardWidth:
    keyboardOffset=0
    boardSpacing=int(((keyboardWidth-emptyWidth)/2))
elif emptyWidth>keyboardWidth:
    keyboardOffset=int((emptyWidth-keyboardWidth)/2)
    boardSpacing=0
else:
    keyboardOffset=0
    boardSpacing=0

advanceTurn=False

# main loop
# if turn exeeds 6 then end loop and show lose screen
while turn<gameLength:
    jint.clear()
    d=0
    c=0
    a=0
    n=0
    # get input
    #print('UNCLEBENWHATHAPPEND :SOBB:',wordLength,impHistory,iterations)
    while True:
        a=0
        if iterations>0:
            imp=input()
        imp=imp.upper().strip()
        #print('[debug] imp=',imp)     
        if len(imp) == wordLength and imp.isalpha():
            if checkWords==True and wordLength==5:
                #print('[debug]',scanList(imp.lower(),content))
                if scanList(imp.lower(),content):
                    impHistory.append(list(imp))
                    break
                else: 
                    messageBuffer=('wtf is \"{0}\" brh').format(imp.lower())
                    advanceTurn=False
                    break
            else:
                impHistory.append(list(imp))
                break
        else: 
            messageBuffer=('{0} letter word gng ts ntb').format(wordLength)
            advanceTurn=False
            break
    # turn input into list for indexing
    imp = list(imp)
    print('\n'*lineClears)
    a=0
    # check answers
    if advanceTurn==True:
        while n<wordLength:
            # if the letter only appears once, check normally
            if imp.count(imp[n])<2:
                marking[turn][n] = evaluate(imp[n],n)
                applyKBV(marking[turn][n],n)
            # if the letter appears twice we gotta do all this
            else:
                # evaluates all instances of nth letter
                # + formats it into list 'jint'
                while a<wordLength:
                    if imp[a]==imp[n]:
                        jint.append(evaluate(imp[a],a))
                    else:
                        jint.append(0)
                    a=a+1
                a=0
                c=0
                d=0
                #print('[debug] 1stcheck, iteration:',n,d,jint)
                # goes through list 'jint' and checks for greens
                while c < correctWord.count(imp[n]):
                    if jint[d] == 2:
                        marking[turn][d] = 2
                        applyKBV(2,n)
                        c=c+1
                    d=d+1
                    if d>(wordLength-1):
                        break
                # goes through list 'jint' and checks for yellows
                d=0
                while c < correctWord.count(imp[n]):
                    if jint[d] == 1:
                        marking[turn][d] = 1
                        applyKBV(1,n)
                        c=c+1
                    d=d+1
                    if d>(wordLength-1):
                        break
            #print('[debug] 2ndcheck, iteration:',n,jint)
            jint.clear()
            n=n+1
    jint.clear()
    d=0
    c=0
    a=0
    n=0
    # print + format results
    while n<len(impHistory):
        #print prev guesses + answers
        #print('[debug] impHistory:',impHistory)
        #print('[debug] turn:',turn)
        print(' '*boardSpacing,end='')
        for m in range(wordLength):
            if marking[n][m]==1:
                print('\033[93m','(',impHistory[n][m],')','\033[0m',sep='',end='')
            elif marking[n][m]==2:
                print('\033[92m','{',impHistory[n][m],'}','\033[0m',sep='',end='')
            else:
                print('[',impHistory[n][m],']',sep='',end='')
        if n==0:
            print('   ',messageBuffer)
        else:
            print('')
        n=n+1
    # repeat gameLength-n
    a=0
    while a<(gameLength-n):
        #print remaining empty boxes
        #print('[debug] n=',n)
        print(' '*boardSpacing,'[ ]'*wordLength,sep='',end='')
        if a==0 and n==0:
            #issue: "messagebuffer" prints "5 letter word gng ts ntb"
            #cause: idfk
            if iterations==0:   
                print('    type a word')
            else:   
                print('   ',messageBuffer)
        else:
            print('')
        a=a+1


    #print and format the keyboard
    printKeyboard(keyboardOffset)

    #print('[debug]',marking)
    #print('[debug]',impHistory)


    # check for win
    if marking[turn]==([2]*wordLength):
        print('you are win :) (yay)\n')
        s.close()
        exit()
    # advance turn
    #print('[debug] adavanceturn', advanceTurn)
    if advanceTurn==True:
        turn=turn+1
    messageBuffer="type a word"
    advanceTurn=True
    iterations=iterations+1
    
# print format losing condition
n=0
print('  you are lose :(\nthe word was:',end=' ')
for n in range(wordLength):
    print(correctWord[n],end='')
print('')
s.close()





# centre keyboard on the word thing.
# this means getting the width of the word selecter, 
# subtracting it from the width of the first line of the keyboard, 
# and then adding that/2 before the keyboard is printed

#(''.join(keyboard)).sep('\n')
#(wordLength*3)+2