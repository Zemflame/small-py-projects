# this project is mostly filled with pseudocode and notes
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






def evaluate(letter,index):
    if letter == correctWord[index]:
        marking[turn][index] = 2
        greenLetters.add(letter)
    elif letter in correctWord:
        marking[turn][index] = 1
        greenLetters.add(letter)
    else: 
        greyLetters.add(letter)




n=0


(imp.count(imp[n])-correctWord.count(imp[n]))
#
#(instances of A in "guess" - instances of A in "correct")
g = ABCDE
c = BAACD
will be negative -> evaluate normally

g = ABCDE
c = ABCDE
will be zero -> evaluate normally

g = BAACD
c = ABCDE
will be +1 -> complex

g = BAAAD
c = ABADE
will be +1 -> complex evaluation

g = BACDA
c = ABCDA
will be zero -> simple evaluation

g = BACDA
c = ABCDE
will be 1 -> complex evaluation

g = BAACD
c = EBCDA
will be +1 -> only

g = BAACD
c = EBADC
will be +1 -> only

mc = 10211
mb = 11211
mB = 11011

# limit how many times it can check by how many instances of the letter there are.
# prioritise green.

# mark individually but then save to different list
# different list formatting:
# always 5 long
# spots where letter didnt show up are 0
# spots where the letter was yellow are 1
# spots where the letter was green are 2

# look through list (correctWord.count(imp[n]) times.
# when it sees green: add to "marking" in the given position, go to start of loop and increase counter
# once it has seen all green or there is no green, do the same for yellow until it stops looping.
# this should yeild correct results


#example:

g = BAACD
c = EBADC

#goes through imp[0] (B):
# -finds 1 instance of B in imp
# -adds to "marking[turn][n]"

#goes through imp[1] (A):
# -finds 2 instances of A in imp
# -creates new list called jint
# -fills jint with:
# [0,1,2,0,0]
# ^ gets this by doing simple evaluation for every instance of A 
#and filling the rest with 0
# -loops through jint the number of times A appears in correctWord (1 time)
# -1st loop:
#   is jint[0] green? - no
#   is jint[1] green? - no
#   is jint[2] green? - yes
#       marking[turn][2] = 2
#       reduce loopcount by 1
#       go to start
# -2nd loop (if there was one)
#   is jint[0] yellow? - no
#   is jint[1] yellow? - yes
#       marking[turn][1] = 1
#       reduce loopcount by 1
#       go to start
# -loop ends, delete all of jint list
jint=[]
while n<5:
    if imp.count(imp[n])<2:
        evaluate(imp[n],n)
    else:
        for letter in imp:
            if letter==imp[n]:
                jint.append(evaluate(letter,n))
            else:
                jint.append(0)
    n=n+1
,
print(jint)




#times imp[n] appears in correctWord is how many letters can be marked as != grey



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



    #only simple evaluate each letter the number of times it shows up in the correct word, otherwise leave it

    repeat imp.count(imp[n]):
        evaluate(imp[n], n)





# n = index of the letter we are focusing on

# if imp[n] shows up more than one time, locate the places it shows up and put them in a list
# to store them, go through each item in imp and if its the same as imp[n], add its index to the list
placesItShowsUp = []
imp = ['A','B','A','T','E']


#collect places that imp[n] shows up
if imp.count(imp[n])>1:
    q=0
    for q in range(5)
        if imp[n]==imp[q]:
            placesItShowsUp.append(q)
else:
    evaluate(imp[n],n)

for w in placesItShowsUp:
    evaluate(imp[n],imp[w])


# run evaluate() for the letter and index 1 placesItShowsUp
# run evaluate() for the letter and index 2 placesItShowsUp
# run evaluate() for the letter and index 3 placesItShowsUp
# run evaluate() for the letter and index 4 placesItShowsUp
# placesItShowsUp = [0,2]






# index 1 to imp.count[imp[n]]




