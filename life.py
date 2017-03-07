#life.py

#Brianne Cotter
#3/6/17

#declare and initialize board and newBoard

#assign board with starting configuration

#update new board according to rules,
#refering to board to count number of live neighbors for each cell

#swap board and newBoard

#print contents of board


def createBoard(w, h): #creates a board of zeros with give w and  h
    a = []
    for i in range(w):
        a.append([0]*h)
    print (a)

def startingBoard():
    createBoard()
    
def updateBoard (w, h, a): 
    aliveCounter = 0
    for x in range (0, w-1):
        for y in range (0, h-1): #loop thur board to  
            N = a[((h+(y-1))%h)][x]
            NE = a[((h+(y-1))%h)][(x+10%w)]
            E = a[y][(x+10%w)]
            SE = a[(y+1)%h][(x+10%w)]
            S = a[(y+1)%h]
            SW = a[(y+1)%h][(w+(x-1)%w)]
            W = a[y][(w+(x-1)%w)]
            NW = a[((h+(y-1))%h)][(w+(x-1)%w)]
    if N == 1:
        aliveCounter = aliveCounter + 1
    if NE == 1:
        aliveCounter = aliveCounter + 1
    if E == 1:
        aliveCounter = aliveCounter + 1
    if SE == 1:
        aliveCounter = aliveCounter + 1
    if S == 1:
        aliveCounter = aliveCounter + 1
    if SW == 1:
        aliveCounter = aliveCounter + 1
    if W == 1:
        aliveCounter = aliveCounter + 1
    if NW == 1:
        aliveCounter = aliveCounter + 1
    if aliveCounter == 1 or aliveCounter == 0:
        a[y][x] = 0
    if aliveCounter == 2:
        return a[y][x]
    if aliveCounter == 3:
        a[y][x]= 1
    if aliveCounter >= 4:
        a[y][x] = 0

def newBoard(w, h, a):
    updateBoard(w, h, a[y][x])
    print(a)
    
def main():
    height = 10
    width = 10
    h = height
    w = width
    ROUNDS = 5
    while ROUNDS <= 5:
        startingBoard(w, h)
        updateBoard(w, h, a)
        newBoard(w, h, a)
        ROUNDS = ROUNDS + 1

if __name__ == '__main__':
    main()
