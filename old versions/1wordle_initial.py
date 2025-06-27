# this project is in a presentable state
# made w/o any chatgpt
# the marking is currently not 
# 100% accurate to real wordle

# in the interest of optimisation
# i have made it so you can type anything
# as adding word checking would warrent
# checking through a 13,000 line text document
# every time the user types a word
# which is not very nice for the old cpu
# however a similar thing has been implemented
# for the word random choosing


import random
n=0
a=0
v=0
imp=''
turn = 0
marking = [0,0,0,0,0]

# getting random word
with open("potentialAnswers", "rt") as s:
    content = s.readlines()
correctWord = list(content[random.randint(0,2314)])[0:5]


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
        if len(imp) == 5:
            break
        else: print('actually type 5 characters bro')


    imp = list(imp)
    # check answers
    n=0
    while n<5:
        a=0
        if imp[n] == correctWord[n]:
            marking[n] = 2
        else:
            while a<5:
                if imp[n] == correctWord[a]:
                    marking[n] = 1
                    break
                else:
                    a=a+1
        n=n+1
    v=0

    # print + format results
    while v<5:
        if marking[v]==0:
            print('[',imp[v],']',sep='',end='')
        elif marking[v]==1: 
            print('(',imp[v],')',sep='',end='')
        else: print('{',imp[v],'}',sep='',end='')
        v=v+1
    print('')
    turn=turn+1
    # check for win
    if marking==[2,2,2,2,2]:
        print('you are win yay')
        exit()
    marking = [0,0,0,0,0]
    
# format losing condition
print('you are lose :(\nthe word was',end=' ')
print(correctWord[0],end='')
print(correctWord[1],end='')
print(correctWord[2],end='')
print(correctWord[3],end='')
print(correctWord[4])