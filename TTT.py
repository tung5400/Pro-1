#Import
import os
os.system("cls")
import random
# Creating board
def printBoard():
    print('=-----------------------')
    print('|r\c |  0  |  1  |  2  |')
    print('------------------------')
    print('| 0  |  {}  |  {}  |  {}  |'.format(board[0][0], board[0][1], board[0][2]))
    print('------------------------')
    print('| 1  |  {}  |  {}  |  {}  |'.format(board[1][0], board[1][1], board[1][2]))
    print('------------------------')
    print('| 2  |  {}  |  {}  |  {}  |'.format(board[2][0], board[2][1], board[2][2]))
    print('------------------------')

# Check win
def check():
    for i in range(0,3):
        if board[i][0]==board[i][1]==board[i][2]==player['1'] or board[0][i]==board[1][i]==board[2][i]==player['1']:
            return 1
        elif (board[i][0]==board[i][1]==board[i][2]==player['2']) or (board[0][i]==board[1][i]==board[2][i]==player['2']):
            return 2
    if board[0][0]==board[1][1]==board[2][2]==player['1'] or board[2][0]==board[1][1]==board[2][0]==player['1']:
        return 1
    elif board[0][0]==board[1][1]==board[2][2]==player['2'] or board[2][0]==board[1][1]==board[2][0]==player['2']:
        return 2
    return 0
    
#Input Board
def inputboard(st, r):
    while (len(st)<=2) or (len(st)>=4):
        print('Please insert a correct coordinates of an empty block:')
        st=input()
    x, y = (int(num) for num in st.split())
    while board[x][y] != ' ' or y==None:
        print('Please insert a correct coordinates of an empty block:')
        x, y = (int(num) for num in st.split())
    board[x][y]=player[str(r)] 
    
# Random
def rando():
    global c
    c=random.randint(1,2)
    if c==1:
        print('\nPlayer no 1 will get to play first')
    else:
        print('\nPlayer no 2 will get to play first')
            
# Main
s='Y'
while (s=='Y') or (s=='YES'):
    board=[[" "," "," "],[" "," "," "],[" "," "," "]]
    print('Welcome to a game of TIC TAC TOE!!!')
    print('\nAs player no 1, please choose your mark between X or O, player no 2 will get the other mark\nNow choose: ')
    a=input().upper()
    while (a!='X') and (a!='O'):
        print ('\nPlease choose a mark between X or O: ')
        a=input().upper()
    player={'1':'','2':''}
    if a=='X':
        print('\nSo player no 1 will be represented as X and player no 2 will be represented as O.')
        player['1']='X'
        player['2']='O'
    else:
        print('\nSo player no 1 will be represented as O and player no 2 will be represented as X.')
        player['2']='X'
        player['1']='O'
    rando()
    print('\nThe board will be 3x3 and this is the lay out:')
    printBoard()
    d=0
    while True:
        print('\nPlayer {} \'s turn, please choose a coordinate row then column: '.format(c))
        st=input()
        inputboard(st,c)
        printBoard()
        print(d)
        if check()!=0:
            break
        d+=1
        if d==5:
            break
        print('\nPlayer {} \'s turn, please choose a coordinate row then column: '.format(3-c))
        st=input()
        inputboard(st,3-c)
        printBoard()
        print (d)
        if check()!=0:
            break
    if (d==5):
        print('This is a draw ')
    else:
        print('\nPlayer {} win'.format(check()))
    print('\nDo you both want to player again, choose yes to continue or no to quit: ')
    s=input().upper()
    while (s!='Y') and (s!='N') and (s!='YES') and (s!='NO'):
        print('\nPlease type a correct answer: ')
        s=input().upper()
    os.system('cls')
    if s=='NO'or s=='N':
        print('Game Over')