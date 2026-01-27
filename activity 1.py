'''we will make the board using dictionary
in which keys will be the location(1.e: top-left, mid-right, etc.)
and initially its values will be empty space and then after every move 
we will change the value according to player's choice of move.'''

theBoard = {'7': ' ', '8': ' ','9': ' ',
            '4': ' ', '5': ' ', '6': ' ',
            '1': ' ', '2': ' ', '3': ' '}

board_keys = []

for key in theBoard:
    board_keys.append(key)

''' we will have to print the updated board after every move in the game and thus we will make a function in which well define the printBoard function so that we can easily print the board everytime by calling this function'''

def printBoard(board):
    print(board['7']+'|' + board['8'] + '|' + board['9'])
    print('-+-+-')
    print(board['4']+'|' + board['5'] + '|' + board['6'])
    print('-+-+-')
    print(board['1']+'|' + board['2'] + '|' + board['3'])

def game():

    turn = 'X'
    count = 0

    for i in range(10):
        printBoard(theBoard)
        print("it's your turn," + turn + ".Move to which place?")

        move = input()

        if theBoard[move] == ' ':
            theBoard[move] = turn
            count+= 1
        else:
            print("that place is already filled.|nMove to which place?")
            continue

        if count >= 5:
            if theBoard['7'] == theBoard['8'] == theBoard['9'] != ' ':
                printBoard(theBoard)
                print("|nGame Over.|n")
                print(" **** " +turn +" won. ****")
                break
            elif theBoard['4'] == theBoard ['5'] == theBoard['6'] != ' ':
                printBoard(theBoard)
                print("|nGame Over.|n")
                print(" **** " +turn +" won. ****")
                break
            elif theBoard['1'] == theBoard ['2'] == theBoard['3'] != ' ':
                printBoard(theBoard)
                print("|nGame Over.|n")
                print(" **** " +turn +" won. ****")
                break
            elif theBoard['1'] == theBoard ['4'] == theBoard['7'] != ' ':
                printBoard(theBoard)
                print("|nGame Over.|n")
                print(" **** " +turn +" won. ****")
                break
            elif theBoard['1'] == theBoard ['2'] == theBoard['3'] != ' ':
                printBoard(theBoard)
                print("|nGame Over.|n")
                print(" **** " +turn +" won. ****")
                break
            elif theBoard['1'] == theBoard ['2'] == theBoard['3'] != ' ':
                printBoard(theBoard)
                print("|nGame Over.|n")
                print(" **** " +turn +" won. ****")
                break
            elif theBoard['2'] == theBoard ['5'] == theBoard['8'] != ' ':
                printBoard(theBoard)
                print("|nGame Over.|n")
                print(" **** " +turn +" won. ****")
                break
            elif theBoard['3'] == theBoard ['6'] == theBoard['9'] != ' ':
                printBoard(theBoard)
                print("|nGame Over.|n")
                print(" **** " +turn +" won. ****")
                break
            elif theBoard['7'] == theBoard ['5'] == theBoard['3'] != ' ':
                printBoard(theBoard)
                print("|nGame Over.|n")
                print(" **** " +turn +" won. ****")
                break
            elif theBoard['1'] == theBoard ['5'] == theBoard['9'] != ' ':
                printBoard(theBoard)
                print("|nGame Over.|n")
                print(" **** " +turn +" won. ****")
                break

            
        if count == 9:
                print("\nGame Over.\n")
                print("it's a Tie!")

        if turn == 'X' :
                turn = 'O'
        else:
                turn = 'X'

    restart = input("do you want to play again?(y/n)")
    if restart == "y" or restart == "Y":
        for key in board_keys:
            theBoard [key] = " "

        game()

if __name__ == "__main__":
    game()




