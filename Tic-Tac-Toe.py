
#-----------------------Welcome to tic tac toe----------------------
import math as m
import random as rd

print('Welcome to the Game \nCurrently all your grids are empty');

tic_tac_toe=[[None,None,None],[None,None,None],[None,None,None]];
# axis1=2
# axis2=2
# tic_tac_toe[axis1][axis2]=2
# print(tic_tac_toe)

def sum_row(tic_tac):
    count_0=0
    count_1=0
    for i in tic_tac:
        for y in i:
            if y!=None:
                if y==1:
                    count_1+=1
                else:
                    count_0+=1

        if count_1==3 or count_0==3:
            return 1
        else:
            count_0=0
            count_1=0
    return -1

def sum_col(tic_tac):
    count_0=0
    count_1=0
    for i in range(0,3):
        for j in range(0,3):
            y=tic_tac[j][i]
            if y!=None:
                if y==1:
                    count_1+=1
                else:
                    count_0+=1

        if count_1==3 or count_0==3:
            return 1
        else:
            count_0=0
            count_1=0
    return -1


def sum_diag_left(tic_tac):
    count_0 = 0
    count_1 = 0
    for i in range(0, 3):
        y = tic_tac[i][i]
        if y != None:
            if y == 1:
                count_1 += 1
            else:
                count_0 += 1

    if count_1 == 3 or count_0 == 3:
        return 1
    return -1

def sum_diag_right(tic_tac):
    count_0 = 0
    count_1 = 0
    j=0
    for i in range(3, 0,-1):

        y = tic_tac[j][i-1]
        #print(y)
        if y != None:
            if y == 1:
                count_1 += 1
            else:
                count_0 += 1
        j=j+1

    if count_1 == 3 or count_0 == 3:
        return 1
    return -1

#print(sum_diag_right(tic_tac_toe))



for i in tic_tac_toe:
    for y in i:
        if y==None:
            print('-',end='\t')
        else:
            print(y)
    print('\n')

val=1;
print('This is what your grid represents:')
for i in range(0,3):
    for y in range(0,3):
        print(val,end='\t');
        val=val+1
    print('\n')

print('Game on:\n')
user_1=input('User 1: Please enter your name:\n');
user_2=input('User 2: Please enter your name:\n');
print('Welcome',user_1,' and ',user_2)

print('Lets randomize your choice:')
rand=rd.random()
if rand>0.5:
    print(user_1,' 1 is used to fill your grid and ',user_2, ' 0 is used to fill your grid');
    choice1=1
    choice2=0
else:
    print(user_1,' 0 is used to fill your grid and ',user_2, ' 1 is used to fill your grid');
    choice1 = 0
    choice2 = 1

val=0
axis1=None
axis2=None
usr=1

for game in range(1,10):
    if usr%2==1:
        print(user_1, 'your turn to select a grid. Select any range between 1 and 9\n')
        first_cor=int(input('Enter grid\n'))
        usr=usr+1
    else:
        print(user_2, 'your turn to select a grid. Select any range between 1 and 9\n')
        first_cor = int(input('Enter grid\n'))
        usr=usr+1

    for i in range(0, 3):
        for y in range(0, 3):
            if (val+1)==first_cor:
                axis1=i
                axis2=y
                #print(axis1)
                #print(axis2)
                val=0
                break
            else:
                val = val + 1
        if val==0:
            break

    if (usr%2)==1:
        tic_tac_toe[axis1][axis2]=choice1
    else:
        tic_tac_toe[axis1][axis2]=choice2

    for i in tic_tac_toe:
        for y in i:
            if y==None:
                print('-',end='\t')
            else:
                print(y, end='\t')
        print('\n')

    if sum_row(tic_tac_toe)==1 or sum_col(tic_tac_toe)==1 or sum_diag_left(tic_tac_toe)==1 or sum_diag_right(tic_tac_toe)==1:
        print('Game Ends')
        break
    else:
        if game==8:
            print('Draw')
