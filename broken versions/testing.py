



keyboard=[
    '\n','Q','W','E','R','T','Y','U','I','O','P',
    '\n ','A','S','D','F','G','H','J','K','L',
    '\n   ','Z','X','C','V','B','N','M']

#keyboard=[
#    '\n ','Q','W','F','P','B','J','L','U','Y',
#    '\n','A','R','S','T','G','M','N','E','I','O',
#    '\n   ','Z','X','C','D','V','K','H'
#]

#qwfpbjluy; arstgmneio zxcdvkh,./

wordLength=0

#((wordlength*3)+2) - (len((''.join(keyboard)).split('\n')[0])*2)

greenLetters=set()
yellowLetters=set()
greyLetters=set()






keyboardWidth = max( (len((''.join(keyboard[1:])).split('\n')[0])*2),(len((''.join(keyboard[2:])).split('\n')[0])*2),(len((''.join(keyboard[3:])).split('\n')[0])*2),)-1
emptyWidth=((wordLength*3)+2)


#if emptyWidth<keyboardWidth:
#    keyboardOffset=0
#    emptyOffset=int((keyboardWidth-emptyWidth)/2)
#elif emptyWidth>keyboardWidth:
#    keyboardOffset=int((emptyWidth-keyboardWidth)/2)
#    emptyOffset=0
#else:
#    keyboardOffset=0
#    emptyOffset=0



keyboardOffset=abs(emptyWidth-key)

#print(' ','[ ]'*wordLength,sep='',end='')
#print('')

#x=0
#while x<len(keyboard):
#    if keyboard[x]=="\n"
#    elif keyboard[x] in greenLetters:
#    print('\033[92m',keyboard[x],'\033[0m',sep='',end=' ')
#    elif keyboard[x] in yellowLetters:
#    print('\033[93m',keyboard[x],'\033[0m',sep='',end=' ')
#    elif keyboard[x] in greyLetters:
#    print('\033[90m',keyboard[x],'\033[0m',sep='',end=' ')
#    else: print(x,end=' ')

(  ((wordLength*3)+2) - len((''.join(keyboard[1:])).split('\n')[0])*2  )


#piss=['one','TWO','321']

#print(piss[0][2:])

def printKeyboard(preSpacing):
    for x in keyboard:
        if x[0:1]=="\n": print('\n',' '*(preSpacing),x[1:],sep='',end='')
        elif x in greenLetters: print('\033[92m',x,'\033[0m',sep='',end=' ')
        elif x in yellowLetters: print('\033[93m',x,'\033[0m',sep='',end=' ')
        elif x in greyLetters: print('\033[90m',x,'\033[0m',sep='',end=' ')
        else: print(x,end=' ')
    print('\n')
#print(int((wordAreaWidth-keyboardTopRowWidth)/2))

def printEmpty(preSpacing):
    for x in range(4):
        print(' '*preSpacing,'[ ]'*wordLength,sep='',end='\n')
    print(' '*preSpacing,'[ ]'*wordLength,sep='',end='')

while wordLength<20:
    printEmpty(emptyOffset)
    printKeyboard(keyboardOffset)
    print('')
    wordLength=wordLength+1
    emptyWidth=((wordLength*3))
    
    if emptyWidth<keyboardWidth:
        keyboardOffset=0
        emptyOffset=int((keyboardWidth-emptyWidth)/2)
    elif emptyWidth>keyboardWidth:
        keyboardOffset=int((emptyWidth-keyboardWidth)/2)
        emptyOffset=0
    else:
        keyboardOffset=0
        emptyOffset=0



