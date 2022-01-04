# Siddharth Shah
import sys, time

global possibleGames, numBoards, winX, winO, draw
possibleGames, possibleBoards, winX, winO, draw = 0, {}, set(), set(), set()
# PossibleBoards as CACHE for PossibleGames

def setGlobals(h, w):
    horiz = [[*range(i, i+w)] for i in range(0, h*w, w)]
    vert = [[*range(i, h*w, w)] for i in range(0, w)]
    mainDiag = [[idx for idx in range(i, h*w, 1+w) if idx%w - i%w == idx//w - i//w] for i in range(0, w*h) if not i//w or not i%w]
    offDiag = [[idx for idx in range(i, h*w, w-1) if i%w - idx%w == idx//w - i//w] for i in range(0, w*h) if not i//w or i%w == w-1]
    CONSTRAINTS = horiz + vert + mainDiag + offDiag
    idxCONST = [[] for i in range(h*w)]
    for const in CONSTRAINTS:
        for idx in const:
            idxCONST[idx].append(const)
    return CONSTRAINTS, idxCONST

def bruteForce(board, turnNum, lastIdx):
    if board in possibleBoards: return possibleBoards[board]
    if gameOver(board, lastIdx): 
        possibleBoards[board] = 1
        return possibleBoards[board]
    possibleBoards[board] = 0
    for newBoard, newIdx in setOfChoices(board, turnNum):
        possibleBoards[board] += bruteForce(newBoard, turnNum+1, newIdx)
    return possibleBoards[board]

def gameOver(board, lastIdx):
    global winX, winO, draw
    if lastIdx == -1: return False # Once when called
    for const in idxCONST[lastIdx]:
        values = [board[idx] for idx in const]
        for sliceStart in range(len(values)-toWIN+1):
            inserted = values[sliceStart:sliceStart+toWIN]
            if inserted == checkX: 
                winX.add(board)
                return True
            elif inserted == checkO:
                winO.add(board)
                return True
    if "." not in board: # Reached Draw
        draw.add(board)
        return True
    return False

def setOfChoices(board, turnNum):
    setChoices, sym = set(), SYMS[turnNum%2]
    for idx in range(len(board)):
        if board[idx] != ".": continue
        setChoices.add(("".join([board[:idx], sym, board[idx+1:]]), idx))
    return setChoices

def printFinalCounts():
    global possibleGames, possibleBoards, winX, winO, draw
    print("Possible Games: {}".format(possibleGames))
    print("Possible Boards: {}".format(len(possibleBoards)))
    print("Terminal Boards: {}".format(len(winX)+len(winO)+len(draw)))
    print("Win X: {}".format(len(winX)))
    print("Win O: {}".format(len(winO)))
    print("Draw: {}".format(len(draw)))

def printPzl(board, w):
    for idx in range(0, len(board), w): print(" ".join([*board[idx:idx+w]]))

startTime = time.time()
SYMS, turnNum = "xo", 0
toWIN = int(sys.argv[1])
checkX, checkO = ["x" for i in range(toWIN)], ["o" for i in range(toWIN)]
HEIGHT, WIDTH = int(sys.argv[2]), int(sys.argv[3])
board = "".join(["." for i in range(HEIGHT*WIDTH)])
CONSTRAINTS, idxCONST = setGlobals(HEIGHT, WIDTH)
possibleGames = bruteForce(board, 0, -1)
printFinalCounts()
print("Time: {}s".format(round(time.time()-startTime,3)))

# All diagonals are valid diagonals 

# 012
# 345
# 678
# 9 10 11

# 0 1 2 3
# 4 5 6 7
# 8 9 10 11
# 12 13 14 15
# 16 17 18 19

# 0123
# 4567
