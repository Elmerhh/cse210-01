"""This is the tic-tac-toe"""
# We defined a list called numbers 
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

def main():
   
    print("...::: THIS IS THE TIC TAC TOE :::...")
    print()
    #Show the interface
    tablero()
    print()
    #Ask the user choose the number
    selection_user(-1)


def tablero():
    print (f'          {numbers[0]} | {numbers[1]} | {numbers[2]}')
    print (f'          --+---+--')
    print (f'          {numbers[3]} | {numbers[4]} | {numbers[5]}')
    print (f'          --+---+--')
    print (f'          {numbers[6]} | {numbers[7]} | {numbers[8]}')

def selection_user(user):
    while user >= -1 and user < 10:
        user=int(input("O's turn to choose a square ( 1 - 9): "))   
        # Get the index of the value of the user choose.
        i = numbers.index(user)
        numbers[i] = "O"
        tablero()
        win_o_conditions()
        win_x_conditions()
        user=int(input("X's turn to choose a square ( 1 - 9): "))
        i = numbers.index(user)
        numbers[i] = "X"
        tablero()
        win_o_conditions()
        win_x_conditions()



def win_o_conditions():
    if numbers[0] == "O" and numbers[1] == "O" and numbers[2] == "O":
        print (f'CONGRATULATIONS "O" WINS ....!!!!!!')
    elif numbers[0] == "O" and numbers[4] == "O" and numbers[8] == "O":
        print (f'CONGRATULATIONS "O" WINS ....!!!!!!')
    elif numbers[0] == "O" and numbers[3] == "O" and numbers[6] == "O":
        print (f'CONGRATULATIONS "O" WINS ....!!!!!!')
    elif numbers[1] == "O" and numbers[4] == "O" and numbers[7] == "O":
        print (f'CONGRATULATIONS "O" WINS ....!!!!!!')
    elif numbers[2] == "O" and numbers[4] == "O" and numbers[6] == "O":
        print (f'CONGRATULATIONS "O" WINS ....!!!!!!')
    elif numbers[2] == "O" and numbers[5] == "O" and numbers[8] == "O":
        print (f'CONGRATULATIONS "O" WINS ....!!!!!!')
    elif numbers[3] == "O" and numbers[4] == "O" and numbers[5] == "O":
        print (f'CONGRATULATIONS "O" WINS ....!!!!!!')
    elif numbers[6] == "O" and numbers[7] == "O" and numbers[8] == "O":
        print (f'CONGRATULATIONS "O" WINS ....!!!!!!')


def win_x_conditions():
    if numbers[0] == "X" and numbers[1] == "X" and numbers[2] == "X":
        print (f'CONGRATULATIONS "X" WINS ....!!!!!!')
    elif numbers[0] == "X" and numbers[4] == "X" and numbers[8] == "X":
        print (f'CONGRATULATIONS "X" WINS ....!!!!!!')
    elif numbers[0] == "X" and numbers[3] == "X" and numbers[6] == "X":
        print (f'CONGRATULATIONS "X" WINS ....!!!!!!')
    elif numbers[1] == "X" and numbers[4] == "X" and numbers[7] == "X":
        print (f'CONGRATULATIONS "X" WINS ....!!!!!!')
    elif numbers[2] == "X" and numbers[4] == "X" and numbers[6] == "X":
        print (f'CONGRATULATIONS "X" WINS ....!!!!!!')
    elif numbers[2] == "X" and numbers[5] == "X" and numbers[8] == "X":
        print (f'CONGRATULATIONS "X" WINS ....!!!!!!')
    elif numbers[3] == "X" and numbers[4] == "X" and numbers[5] == "X":
        print (f'CONGRATULATIONS "X" WINS ....!!!!!!')
    elif numbers[6] == "X" and numbers[7] == "X" and numbers[8] == "X":
        print (f'CONGRATULATIONS "X" WINS ....!!!!!!')

        
#call main to start this program. 
if __name__ =="__main__":
    main()
