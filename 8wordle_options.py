# THIS PROJECT IS DONE

# made w/o any chatgpt whatsoever
# the marking is 100% accurate to real wordle
# it took like 4 hours to get it correctx

# in the interest of optimisation
# i have made it so you can type anything
# as adding word checking would warrent
# checking through a 13,000 line text document
# every time the user types a word
# which is not very nice for the old cpu
# poor lil guy has to check 76.1kb of data
# however file managaing has been implemented
# for the word random choosing
# which is basically 99% of the challenge
# of implementing word checking

# this /might/ work out of the box
# with more than 5 letters but idk ill try tmr



import random
# importandt variables
gameLength=6
wordLength=5
wordchecking=False

# iterating variables
n=0
a=0
c=0
d=0
m=0

# lists n stuff
jint=[]
imp=''
impHistory=[]
turn = 0
greyLetters=set()
yellowLetters=set()
greenLetters=set()
keyboard=[
    'Q','W','E','R','T','Y','U','I','O','P','\n',
    'A','S','D','F','G','H','J','K','L','\n  ',
    'Z','X','C','V','B','N','M']

# individual word checking
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



while True:
    print('\n\n\n    -- WORDLE --\n>1| PLAY\n>2| options')
    imp=input('')
    imp=imp.lower().strip()

    if (imp=='options') or (imp=='o') or (imp=='2'):
        while True:
            print('\n\n\n - OPTIONS - \nchoose an option to change:'
            '\n>1| gameLenth:',gameLength,
            '\n>2| wordLengh:',wordLength,
            '\n>3| BACK')

            imp=input('')
            imp=imp.lower().strip()

            if (imp=='gamelength') or (imp=='g') or (imp=='1'):
                while True:
                    imp=input('\n\n\ntype a value for gameLength:\n')
                    if imp.isnumeric():
                        if (int(imp)>0):
                            gameLength=int(imp)
                            break
                        else:
                            print('did you really just try to\nmake the game 0 rounds long bruh\ntry think how thats gonna work out')
                            continue
                    else:
                        print('type an integer')
                imp=''
                
            elif (imp=='wordlength') or (imp=='w') or (imp=='2'):
                while True:
                    imp=input('\n\n\ntype a value for wordLength:\n')
                    if imp.isnumeric():
                        if (int(imp)>1):
                            wordLength=int(imp)
                            break
                        else:
                            print('we gon stick to\n2 letter words for now\n')
                            continue
                    else:
                        print('type an integer')
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


print('\n'*15,'    -- WORDLE --\nenter your first guess:\n')

# main loop
# if turn exeeds 6 then end loop and show lose screen
while turn<gameLength:
    jint.clear()
    d=0
    c=0
    a=0
    n=0
    # get input
    while True:
        imp=input('       ')
        imp=imp.upper().strip()
        if len(imp) == wordLength and imp.isalpha():
            impHistory.append(list(imp))
            break
        else: print(wordLength,'letter word gng its not that hard')
    # turn input into list for indexing
    imp = list(imp)
    print('\n')

    # check answers
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
    while n<turn+1:
        #print prev guesses + answers
        #THIS IS FASTER THAN USING AN ADDITIONAL VARIABLE
        #just trust fr
        print('  ',end='')
        for m in range(wordLength):
            if marking[n][m]==1:
                print('\033[93m','(',impHistory[n][m],')','\033[0m',sep='',end='')
            elif marking[n][m]==2:
                print('\033[92m','{',impHistory[n][m],'}','\033[0m',sep='',end='')
            else:
                print('[',impHistory[n][m],']',sep='',end='')
        print('')
        n=n+1
    n=0
    
    while n<((gameLength-1)-turn):
        #print remaining empty boxes
        print(' ','[ ]'*wordLength)
        n=n+1


    #print and format the keyboard; very proud of this section
    print('')
    # loop through each letter in the order of "keyboard"
    for x in keyboard:
        # check if letter is in set "greenletters"
        if x in greenLetters:
            print('\033[92m',x,'\033[0m',sep='',end=' ')
        # check if letter is in set "yellowletters"
        elif x in yellowLetters:
            print('\033[93m',x,'\033[0m',sep='',end=' ')
        # check if letter is in set "greyletters"
        elif x in greyLetters:
            print('\033[90m',x,'\033[0m',sep='',end=' ')
        # otherwise print letter noramlly
        else: print(x,end=' ')
    print('')

    #print('[debug]',marking)
    #print('[debug]',impHistory)


    # check for win
    if marking[turn]==([2]*wordLength):
        print('you are win (yay) :)\n')
        exit()
    # advance turn
    turn=turn+1
    
# print format losing condition
n=0
print('  you are lose :(\nthe word was:',end=' ')
for n in range(wordLength):
    print(correctWord[n],end='')
print('')