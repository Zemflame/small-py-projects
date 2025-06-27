# this project is in a presentable state
# made w/o any chatgpt whatsoever
# the marking is currently not 
# 100% accurate to real wordle but whatever

# in the interest of optimisation
# i have made it so you can type anything
# as adding word checking would warrent
# checking through a 13,000 line text document
# every time the user types a word
# which is not very nice for the old cpu
# poor lil guy has to check 76.1kb of data
# however file managaing has been implemented
# for the word random choosing
# which is basically the same thing




import random
n=0
a=0
imp=''
impHistory=[]
turn = 0
marking = [
    [0,0,0,0,0],
    [0,0,0,0,0],
    [0,0,0,0,0],
    [0,0,0,0,0],
    [0,0,0,0,0],
    [0,0,0,0,0]
]


greyLetters=set()
yellowLetters=set()
greenLetters=set()

keyboard=[
    'Q','W','E','R','T','Y','U','I','O','P','\n',
    'A','S','D','F','G','H','J','K','L','\n  ',
    'Z','X','C','V','B','N','M']

# getting random word
with open("potentialAnswers", "rt") as s:
    content = s.readlines()
    correctWord = list(content[random.randint(0,2314)].upper())[0:5]

#print('[debug]', correctWord)

# intro screen
print('enter your first guess:')

# main loop
# if turn exeeds 6 then end loop and show lose screen
while turn<6:
    # get input
    while True:
        imp=input('       ')
        imp=imp.upper().strip()
        if len(imp) == 5 and imp.isalpha():
            impHistory.append(list(imp))
            break
        else: print('5 letter word gng its not that hard')
    # turn input into list for indexing
    imp = list(imp)
    print('\n')

    # check answers
    n=0
    while n<5:
        a=0
        # check if letter is correct
        if imp[n] == correctWord[n]:
            marking[turn][n] = 2
            greenLetters.add(imp[n])
        else:
            # if not check if its somewhere else
            while a<5:
                if imp[n] == correctWord[a]:
                    marking[turn][n] = 1
                    yellowLetters.add(imp[n])
                    break
                else:
                    # if none of the above make it grey
                    greyLetters.add(imp[n])
                    a=a+1
        n=n+1


    # print + format results
    n=0
    while n<turn+1:
        #print prev guesses + answers
        #THIS IS FASTER THAN USING AN ADDITIONAL VARIABLE
        print('  ',end='')
        if marking[n][0]==1:
            print('\033[93m','(',impHistory[n][0],')','\033[0m',sep='',end='')
        elif marking[n][0]==2:
            print('\033[92m','{',impHistory[n][0],'}','\033[0m',sep='',end='')
        else:
            print('[',impHistory[n][0],']',sep='',end='')


        if marking[n][1]==1:
            print('\033[93m','(',impHistory[n][1],')','\033[0m',sep='',end='')
        elif marking[n][1]==2:
            print('\033[92m','{',impHistory[n][1],'}','\033[0m',sep='',end='')
        else:
            print('[',impHistory[n][1],']',sep='',end='')
            

        if marking[n][2]==1:
            print('\033[93m','(',impHistory[n][2],')','\033[0m',sep='',end='')
        elif marking[n][2]==2:
            print('\033[92m','{',impHistory[n][2],'}','\033[0m',sep='',end='')
        else:
            print('[',impHistory[n][2],']',sep='',end='')
            
        if marking[n][3]==1:
            print('\033[93m','(',impHistory[n][3],')','\033[0m',sep='',end='')
        elif marking[n][3]==2:
            print('\033[92m','{',impHistory[n][3],'}','\033[0m',sep='',end='')
        else:
            print('[',impHistory[n][3],']',sep='',end='')
            

        if marking[n][4]==1:
            print('\033[93m','(',impHistory[n][4],')','\033[0m',sep='')
        elif marking[n][4]==2:
            print('\033[92m','{',impHistory[n][4],'}','\033[0m',sep='')
        else:
            print('[',impHistory[n][4],']',sep='')
        n=n+1
    n=0
    
    while n<(5-turn):
        #print remaining empty boxes
        print('  [ ][ ][ ][ ][ ]')
        n=n+1


    #print and format keyboard visual; very proud of this section
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
    if marking[turn]==[2,2,2,2,2]:
        print('   you are win yay\n')
        exit()
    # advance turn
    turn=turn+1
    
# print format losing condition
print('   you are lose :(\nthe word was',end=' ')
print(correctWord[0],end='')
print(correctWord[1],end='')
print(correctWord[2],end='')
print(correctWord[3],end='')
print(correctWord[4])