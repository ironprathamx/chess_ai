from core.board import Board

choice=int(input("Enter 1 to start new game and 2 to load a FEN. "))
if (choice==1):
    b=Board()
    b.print_board()
elif (choice==2):
    fen=str(input("Enter FEN string. "))
    b=Board(fen)
    b.print_board()
else:
    print("Invalid input!")

choice2=0
while(choice2!=5):
    choice2=int(input("1. Make a move\n2.Undo move\n3.Get FEN of the board\n4.Change state of board to new FEN\n5.Exit"))
    if choice2==1:
        uci=str(input("Enter UCI string: "))
        resmkmv=b.make_move(uci)
        if(resmkmv==False):
            print("Invalid input!")
        b.print_board()
    if choice2==2:
        resunmv=b.undo_move()
        if(resunmv==False):
            print("Undo Failed!")
        else:
            b.print_board()
    if choice2==3:
        curr_fen=b.get_fen()
        print("FEN of Current Game State: ",curr_fen)
    if choice2==4:
        new_fen=str(input("Enter FEN: "))
        b.load_fen(new_fen)
        b.print_board()

