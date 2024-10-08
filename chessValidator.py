# A dictionary matrix of a chessboard. Keys are spaces and values are peice names.
chessBoard = {'a1': 'bRook', 'a2': 'bKnight', 'a3': 'bBishop', 'a4': 'bQueen', 'a5': 'bKing', 'a6': 'bBishop', 'a7': 'bKnight', 'a8': 'bRook',
              'b1': 'bPawn', 'b2': 'bPawn', 'b3': 'bPawn', 'b4': 'bPawn', 'b5': 'bPawn', 'b6': 'bPawn', 'b7': 'bPawn', 'b8': 'bPawn',
              'c1': ' ', 'c2': ' ', 'c3': ' ', 'c4': ' ', 'c5': ' ', 'c6': ' ', 'c7': ' ', 'c8': ' ',
              'd1': ' ', 'd2': ' ', 'd3': ' ', 'd4': ' ', 'd5': ' ', 'd6': ' ', 'd7': ' ', 'd8': ' ',
              'e1': ' ', 'e2': ' ', 'e3': ' ', 'e4': ' ', 'e5': ' ', 'e6': ' ', 'e7': ' ', 'e8': ' ',
              'f1': ' ', 'f2': ' ', 'f3': ' ', 'f4': ' ', 'f5': ' ', 'f6': ' ', 'f7': ' ', 'f8': ' ',
              'g1': 'wPawn', 'g2': 'wPawn', 'g3': 'wPawn', 'g4': 'wPawn', 'g5': 'wPawn', 'g6': 'wPawn', 'g7': 'wPawn', 'g8': 'wPawn',
              'h1': 'wRook', 'h2': 'wKnight', 'h3': 'wBishop', 'h4': 'wQueen', 'h5': 'wKing', 'h6': 'wBishop', 'h7': 'wKnight', 'h8': 'wRook'}

# The main function
def validboard():
    while True:
        totalPeices('w', 'white peice')
        totalPeices('b', 'black peice')
        peiceCheck('white pawn', 'wPawn')
        peiceCheck('black pawn', 'bPawn')
        kingCheck('white king', 'wKing')
        kingCheck('black king', 'bKing')
        validSpace()
        validPeice()
        break

# Verifies that each side has only one king.
def kingCheck(name, peice):
    count = 0
    for x in chessBoard.values():
        if x == peice:
            count = count + 1
    if count < 1 or count > 1 :
        print('Error: ' + name + ' count is invaild')

# Counts the number of pawns.
def peiceCheck(name, peice):
    count = 0
    for x in chessBoard.values():
        if x == peice:
            count = count + 1
    if count > 8 :
        print('Error: ' + name + ' count is invaild')

# Counts the total peices for each side.         
def totalPeices(letter, name):
    count = 0
    for x in chessBoard.values():
        if x[0] == letter:
            count = count + 1
    if count > 16:
        print('Error: ' + name + ' count is invaild')

# Checks that all spaces are valid on the board.
def validSpace():
    spaces = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    for x in chessBoard.keys():
        if x != ' ':
            if x[0] not in spaces:
                print('Some peices are not in the correct letter space')
                
            if int(x[1]) > 8:
                print('Some peices are not in the correct number space')

# Checks the values of peice names.
def validPeice():
    for x in chessBoard.values():
        WorB = ['w', 'b']
        names = ['Pawn', 'Rook', 'Bishop', 'Knight', 'Queen', 'King']
        if x != ' ':
            if x[0] not in WorB:
                print('Peices must be named white or black')
            if x[1:] not in names:
                print('Peices must be named: ' + str(names))
    print('The board is valid')

validboard()