import os

r1=[' ',' ',' ']
r2=[' ',' ',' ']
r3=[' ',' ',' ']

def flipBool(x):
    if x:
        return False
    return True

def setBoard():
    global r1,r2,r3
    r1=[' ',' ',' ']
    r2=[' ',' ',' ']
    r3=[' ',' ',' ']

def setPlayerChoice():
    Player1.setChoice(input(f"{Player1.Pname}, X or O?\n").lower())
    if Player1.Pchoice == 'x' :
        Player2.setChoice("o")
    else:
        Player2.setChoice("x")

def SuccessCombination(r1,r2,r3):
    return [(r1[0],r1[1],r1[2]),
            (r2[0],r2[1],r2[2]),
            (r3[0],r3[1],r3[2]),
            (r1[0],r2[0],r3[0]),
            (r1[1],r2[1],r3[1]),
            (r1[2],r2[2],r3[2]),
            (r1[0],r2[1],r3[2]),
            (r1[2],r2[1],r3[0])]

class Player():
    Pname=None
    Pchoice=None
    Pscore=0
    def __init__(self,name):
        self.Pname=name
    def IncScore(self):
        self.Pscore+=1
    def setChoice(self,choice):
        if choice in ['x','o']:
            self.Pchoice=choice
        else:
            print("Invalid Choice")

def Initialize():
    setPlayerChoice()
    setBoard()
    xturn=True

def PrintBoard():
    os.system('cls')
    print(f"Score:\n{Player1.Pname} : {Player1.Pscore}\n{Player2.Pname} : {Player2.Pscore}\n\nBoard:\t\t\t\t\t\t Positions: \n\t\t\t{r1[0]} | {r1[1]} | {r1[2]} \t\t\t\t7 | 8 | 9\n\t\t\t-- --- --\t\t\t\t-- --- --\n\t\t\t{r2[0]} | {r2[1]} | {r2[2]}\t\t\t\t4 | 5 | 6\n\t\t\t-- --- --\t\t\t\t-- --- --\n\t\t\t{r3[0]} | {r3[1]} | {r3[2]}\t\t\t\t1 | 2 | 3\n")

def entl(x,position):
    global xturn
    if position in [1,2,3]:
        if r3[position-1]==' ':
            r3[position-1]=x
        else:
            print("That position is already occupied")
            xturn=flipBool(xturn)
    elif position in [4,5,6]:
        if r2[position-4]==' ':
            r2[position-4]=x
        else:
            print("That position is already occupied")
            xturn=flipBool(xturn)
    elif position in [7,8,9]:
        if r1[position-7]==' ':
            r1[position-7]=x
        else:
            print("That position is already occupied")
            xturn=flipBool(xturn)
    else:
        print("Invalid input")

def playgame(p1,p2):
    global xturn,GameRst
    if p1.Pchoice=='x':
        xplayer=p1
        oplayer=p2
    else:
        xplayer=p2
        oplayer=p1
    
    if xturn:
        choice=int(input(f"{xplayer.Pname}, x position : "))
        xturn=False
        entl('x',choice)
    else:
        choice=int(input(f"{oplayer.Pname}, o position : "))
        xturn=True
        entl('o',choice)
    for a,b,c in SuccessCombination(r1,r2,r3):
        if a==b and b==c and a==c and a in ['o','x'] and b in ['o','x'] and c in ['o','x']:
            if a=='x':
                xplayer.Pscore+=1
                PrintBoard()
                print(f"\nBingo {xplayer.Pname}, your score : {xplayer.Pscore}\n")
            else:
                oplayer.Pscore+=1
                PrintBoard()
                print(f"\nBingo {oplayer.Pname}, your score : {oplayer.Pscore}\n")
            GameRst=True
            pass

    check_game_over=True

    for r1_,r2_,r3_ in zip(r1,r2,r3):
        if r1_==' ' or  r2_==' ' or r3_==' ':
            check_game_over=False
    
    if check_game_over==True:
        PrintBoard()
        print("Game Over")
        GameRst=True
GameRst=False
Playgame=True

print("Tic Tac Toe\nPositions :\n\t\t\t7 | 8 | 9\n\t\t\t---------\n\t\t\t4 | 5 | 6\n\t\t\t---------\n\t\t\t1 | 2 | 3\nThese are the keys for each position in the board\n")

Player1 = Player(input("Name of player 1 : "))
Player2 = Player(input("Name of player 2 : "))
while True:
    if Player1.Pname==Player2.Pname:
        print("\nName of both players cannot be the same\n")
        Player2 = Player(input("Name of player 2 : "))
    else:
        break

Initialize()

xturn=True

while Playgame:
    os.system('cls')
    PrintBoard()
    playgame(Player1,Player2)

    if GameRst:

        c=input("Do you want to play again?(y/n)").lower()
        if c=="n":
            break
        print("Resetting game...")
        os.system('cls')
        GameRst=False
        Initialize()