# this project is unfinished
# made w/o any chatgpt
# the marking is currently not 
# 100% accurate to real wordle

# in the interest of optimisation
# i have made it so you can type anything
# as adding word checking would warrent
# checking through a 13,000 line text document
# every time the user types a word
# which is not very nice for the old cpu
# however file managaing has been implemented
# for the word random choosing
# which is basically the same thing


import random
n=0
a=0
v=0
t=0
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


# getting random word
with open("potentialAnswers", "rt") as s:
    content = s.readlines()
    correctWord = list(content[random.randint(0,2314)])[0:5]

#print('[debug]', correctWord)

# intro screen
print("wordle :)")
print(r"[A] = grey")
print(r"(A) = yellow")
print(r"{A} = green")
print('enter your first word:')

# main loop
while turn<6:
    # get input
    while True:
        imp=input()
        imp=imp.upper()
        if len(imp) == 5:
            impHistory.append(list(imp))
            break
        else: print('actually type 5 characters bro')


    imp = list(imp)
    print('\n')
    # check answers
    n=0
    while n<5:
        a=0
        if imp[n] == correctWord[n]:
            marking[turn][n] = 2
        else:
            while a<5:
                if imp[n] == correctWord[a]:
                    marking[turn][n] = 1
                    break
                else:
                    a=a+1
        n=n+1
    v=0

    # print + format results
    t=0
    n=0
    #repeat {turn} times
    while n<turn+1:
        #print formatted answers
        #THIS IS FASTER THAN USING AN ADDITIONAL VARIABLE
        if marking[n][0]==1:
            print('(',impHistory[n][0],')',sep='',end='')
        elif marking[n][0]==2:
            print('{',impHistory[n][0],'}',sep='',end='')
        else:
            print('[',impHistory[n][0],']',sep='',end='')


        if marking[n][1]==1:
            print('(',impHistory[n][1],')',sep='',end='')
        elif marking[n][1]==2:
            print('{',impHistory[n][1],'}',sep='',end='')
        else:
            print('[',impHistory[n][1],']',sep='',end='')
            

        if marking[n][2]==1:
            print('(',impHistory[n][2],')',sep='',end='')
        elif marking[n][2]==2:
            print('{',impHistory[n][2],'}',sep='',end='')
        else:
            print('[',impHistory[n][2],']',sep='',end='')
            
        if marking[n][3]==1:
            print('(',impHistory[n][3],')',sep='',end='')
        elif marking[n][3]==2:
            print('{',impHistory[n][3],'}',sep='',end='')
        else:
            print('[',impHistory[n][3],']',sep='',end='')
            

        if marking[n][4]==1:
            print('(',impHistory[n][4],')',sep='')
        elif marking[n][4]==2:
            print('{',impHistory[n][4],'}',sep='')
        else:
            print('[',impHistory[n][4],']',sep='')
        n=n+1
    n=0
    
    while n<(5-turn):
        #print empty boxes
        print('[ ][ ][ ][ ][ ]')
        n=n+1
    


    # check for win
    if marking[turn]==[2,2,2,2,2]:
        print('you are win yay')
        exit()
#    print(marking)
#    print(impHistory)
    turn=turn+1
    
# format losing condition
print('you are lose :(\nthe word was',end=' ')
print(correctWord[0],end='')
print(correctWord[1],end='')
print(correctWord[2],end='')
print(correctWord[3],end='')
print(correctWord[4])