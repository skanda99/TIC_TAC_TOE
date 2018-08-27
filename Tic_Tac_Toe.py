
import random

print()
print('Welcome to Tic Tac Toe!!')
print()

ch_p=None
while ch_p!='X' and ch_p!='O':
    ch_p=input("Choose only ('O' or 'X'): ")

ch_c='O' if ch_p=='X' else 'X'

#print(ch_p,ch_c)

board=[['_','_','_'] for i in range(3)]

valid_index=[(i,j) for i in range(3) for j in range(3)]

print()
print('You play first!')

def display_board ():
    for i in range(3):
        for j in range(3):
            print(board[i][j],end=' ')  
        print()


def valid_entry(a,b):
    if (a,b) in valid_index:
        return True
    return False


def change_board(a,b,ch):
    board[a][b]=ch


def check_win(ch):
    if board[0][0]==board[0][1]==board[0][2]==ch:
        return board[0][0]
    elif  board[1][0]==board[1][1]==board[1][2]==ch:
        return board[1][0]
    elif board[2][0]==board[2][1]==board[2][2]==ch:
        return board[2][0]
    elif board[0][0]==board[1][0]==board[2][0]==ch:
        return board[0][0]
    elif board[0][1]==board[1][1]==board[2][1]==ch:
        return board[0][1]
    elif board[0][2]==board[1][2]==board[2][2]==ch:
        return board[0][2]
    elif board[0][0]==board[1][1]==board[2][2]==ch:
        return board[0][0]
    elif board[0][2]==board[1][1]==board[2][0]==ch:
        return board[0][2]
    else:    
        return  None    
    

def comp_chance():
    
    if board[0][0]==board[2][2]==ch_p or board[2][0]==board[0][2]==ch_p:
        best={(1,0),(2,1),(1,2),(0,1)}
    else:
        best={(0,0),(2,0),(0,2),(2,2),(1,1)}
    

    best_avai=best & set(valid_index)    

    t=utility(ch_c)
    if t==None:
        t=utility(ch_p)

    if t!=None:
        valid_index.remove(t)
        board[t[0]][t[1]]=ch_c   
    
    elif (1,1) in valid_index:
        valid_index.remove((1,1))
        board[1][1]=ch_c  
    
    elif best_avai:
        a,b=random.choice(list(best_avai))
        valid_index.remove((a,b))
        board[a][b]=ch_c 
    else:
        a,b=random.choice(valid_index)
        valid_index.remove((a,b))
        board[a][b]=ch_c
    
                    
        

def utility(ch):
    for i in range(3):
        if board[i].count(ch)==2 and '_' in board[i]:
            return (i,board[i].index('_'))
    cnt=0
    for j in range(3):
        cnt=0
        for i in range(3):
            if board[i][j]==ch:
                cnt+=1     
            else:
                index=i
        if cnt==2 and board[index][j]=='_':
            return (index,j)
    cnt=0
    for i,j in zip(range(3),range(3)):
        if board[i][j]==ch:
            cnt+=1
        else:
            index=i
    if cnt==2 and board[index][index]=='_':
        return (index,index)

    cnt=0
    for i,j in zip(range(3),range(2,-1,-1)):
        if board[i][j]==ch:
            cnt+=1
        else:
            index=i
    if cnt==2 and board[index][2-index]=='_':
        return (index,2-index)

    return None 
  



while valid_index:
   
    try:
        x,y=input('Enter valid 0-based indices (a,b): ').split()
        x=int(x)
        y=int(y)
    except:
        continue
    
    if not valid_entry(x,y):
        continue
    
    valid_index.remove((x,y))
    change_board(x,y,ch_p)

    c=check_win(ch_p)
    if c!=None or (not valid_index):
        break

    comp_chance()
    c=check_win(ch_c)
    display_board()
    if c!=None or (not valid_index):
        break

    



if valid_index:
    if c==ch_p:
            print('Congrats!! You Win!!  :)')
    else:
            print('Oh! You lost! :(')

else:
    print('Tough competition for comp!! The game was a draw!!')
    
