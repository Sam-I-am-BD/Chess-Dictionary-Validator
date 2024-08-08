chessBoard = {'a1': 'bRook', 'a2': 'bKnight', 'a3': 'bBishop', 'a4': 'bQueen', 'a5': 'bKing', 'a6': 'bBishop', 'a7': 'bKnight', 'a8': 'bRook',
              'b1': 'bPawn', 'b2': 'bPawn', 'b3': 'bPawn', 'b4': 'bPawn', 'b5': 'bPawn', 'b6': 'bPawn', 'b7': 'bPawn', 'b8': 'bPawn',
              'c1': ' ', 'c2': ' ', 'c3': ' ', 'c4': ' ', 'c5': ' ', 'c6': ' ', 'c7': ' ', 'c8': ' ',
              'd1': ' ', 'd2': ' ', 'd3': ' ', 'd4': ' ', 'd5': ' ', 'd6': ' ', 'd7': ' ', 'd8': ' ',
              'e1': ' ', 'e2': ' ', 'e3': ' ', 'e4': ' ', 'e5': ' ', 'e6': ' ', 'e7': ' ', 'e8': ' ',
              'f1': ' ', 'f2': ' ', 'f3': ' ', 'f4': ' ', 'f5': ' ', 'f6': ' ', 'f7': ' ', 'f8': ' ',
              'g1': 'wPawn', 'g2': 'wPawn', 'g3': 'wPawn', 'g4': 'wPawn', 'g5': 'wPawn', 'g6': 'wPawn', 'g7': 'wPawn', 'g8': 'wPawn', 'i8': ' ',
              'h1': 'wRook', 'h2': 'wKnight', 'h3': 'wBishop ', 'h4': 'wQueen', 'h5': 'wKing', 'h6': 'wBishop', 'h7': 'wKnight', 'h8': 'wRook'}

def validboard():
    while True:
        totalPeices('w', 'white peice')
        totalPeices('b', 'black peice')
        peiceCheck('white pawn', 'wPawn')
        peiceCheck('black pawn', 'bPawn')
        kingCheck('white king', 'wKing')
        kingCheck('black king', 'bKing')

def kingCheck(name, peice):
    count = 0
    for x in chessBoard.values():
        if x == peice:
            count = count + 1
    if count < 1 or count > 1 :
        print('Error: ' + name + ' count is invaild')
        return False

def peiceCheck(name, peice):
    count = 0
    for x in chessBoard.values():
        if x == peice:
            count = count + 1
    if count > 8 :
        print('Error: ' + name + ' count is invaild')
        return False
        
def totalPeices(letter, name):
    count = 0
    for x in chessBoard.values():
        if x[0] == letter:
            count = count + 1
    if count > 16:
        print('Error: ' + name + ' count is invaild')
        return False
    
validboard()