
# FUNCTION TO DISPLAY THE BOARD AT ANY MOVE
def dispboard(board):
    print("-"*13)
    print("| "+board[7]+" | "+board[8]+" | "+board[9]+" |")
    print("-"*13)
    print("| "+board[4]+" | "+board[5]+" | "+board[6]+" |")
    print("-"*13)
    print("| "+board[1]+" | "+board[2]+" | "+board[3]+" |")
    print("-"*13)

# FUNCTION TO CHECK WHETHER A SPOT ON BOARD IS EMPTY OR NOT
def isempty(board, position):
    return not (board[position] == 'x' or board[position] == 'o')

# FUNCTION TO CHECK WHETHER BOARD IS FILLED OR NOT
def isboardfull(board):
    for i in range(1, 10):
        if isempty(board, i):
            return False
    return True

#FUNCTION TO GET A PLAYER'S MOVE AND CHECK IF IT IS FREE OR NOT

def playerchoice(board, player):
    position = 0
    while position not in range(1, 10) or not isempty(board, position):
        position = int(input("{} Enter your next move\n".format(player)))
    return position

# FUNCTION TO CHECK IF SOMEONE HAS WON OR NOT

def wincheck(board, marker):
    return ((board[7] == board[8] == board[9] == marker) or
            (board[4] == board[5] == board[6] == marker) or
            (board[1] == board[2] == board[3] == marker) or
            (board[1] == board[4] == board[7] == marker) or
            (board[2] == board[5] == board[8] == marker) or
            (board[3] == board[6] == board[9] == marker) or
            (board[7] == board[5] == board[3] == marker) or
            (board[1] == board[5] == board[9] == marker))

# FUNCTION TO ASSIGN A MARKER TO A BOARD BLANK SPACE

def assign(board, marker, position):
    board[position] = marker
    return board

# MAIN FUNCTION OF GAME PLAY

def game():
    print("HELLO! My name is Harshit and this is my first project.")
    print("I hope you enjoy my first self made game and feel free to write your experience and suugestions for improvements, if any, after you finish the game!")
    print("\nWELCOME TO TIC-TAC-TOE! HAVE FUN AND ENJOY THE GAME!")

    print("\n")
    print("This is the board you are going to play on!\n\n\n")
    for i in range(3):
        print("-"*13)
        print("|"+"   "+"|"+"   "+"|"+"   "+"|")
    print("-"*13)
    print("\n")
    print("\nI assume you know the basic rules of Tic Tac Toe, so I am not going to explain them. However, you have to play strictly using X and O only.\n")
    print("The guide board below demonstrates the key you have to press to make a corresponding move on the board.For instance to make a move to the top left corner of the board, press 7. Okay!\n")
    print("-"*13)
    print("|"+" 7 "+"|"+" 8 "+"|"+" 9 "+"|")
    print("-"*13)
    print("|"+" 4 "+"|"+" 5 "+"|"+" 6 "+"|")
    print("-"*13)
    print("|"+" 1 "+"|"+" 2 "+"|"+" 3 "+"|")
    print("-"*13)
    print("\n")

    player1 = ""
    player2 = ""
    player1 = input("Enter player 1 name\n")
    player2 = input("Enter player 2 name\n")

    re = True

    while re:

        ch = ''
        first = ''
        second = ''
        print("\nWe will let the computer decide who will choose between X and O\n")
        dict = {0:player1, 1:player2}
        from random import randint
        ch = dict[randint(0, 1)]
        print(ch+ " has been chosen!")

        if ch == player1:
            first = (input("{}, enter your choice\n".format(ch))).lower()
            if firs == 'x':
                second = 'o'
            elif first == 'o':
                second = 'x'
        else:
            second = (input("{}, enter your choice\n".format(ch))).lower()
            if second == 'x':
                first = 'o'
            elif second == 'o':
                first = 'x'
        print("\n"+player1+" will play with "+first)
        print(player2+" will play with "+second)

        print("\nWe will let the computer decide who makes the first move\n")
        ch = dict[randint(0, 1)]
        print(ch+" will make the first move\n")

        board = ['']*10
        position = 0

        while True:

            if ch == player1:

                position = playerchoice(board, player1)
                board = assign(board, first, position)
                dispboard(board)

                if wincheck(board, first):
                    print("\nCONGRATULATIONS {}!! YOU HAVE WON!!\n".format(player1))
                    break
                elif isboardfull(board):
                    print("IT'S A DRAW! \n")
                    break
                else:
                    ch = player2

            else:

                position = playerchoice(board, player2)
                board = assign(board, second, position)
                dispboard(board)

                if wincheck(board, second):
                    print("\nCONGRATULATIONS {}!! YOU HAVE WON!!\n".format(player2))
                    break
                elif isboardfull(board):
                    print("IT'S A DRAW! \n")
                    break
                else:
                    ch = player1


        choice = (input("Do you want to play again? y/n\n")).lower()
        if choice == 'y':
            re = True
        else:
            re = False
    feedback = input("Thank you for playing the game.\nPlease give your valuable feedback and suggestions, if any.")
game()
