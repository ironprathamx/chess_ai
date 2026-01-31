from core.board import Board
from engine.stockfish_engine import get_best_move

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
while(choice2!=6):
    choice2=int(input("1. Make a move\n2. Let Stockfish make a move\n3. Undo move\n4. Get FEN of the board\n5. Change state of board to new FEN\n6. Exit"))
    if choice2==1:
        uci=str(input("Enter UCI string: "))
        resmkmv=b.make_move(uci)
        if(resmkmv==False):
            print("Invalid input!")
        b.print_board()
    elif choice2==2:
        move=get_best_move(b.get_fen())
        success=b.make_move(move)
        if(success):
            print("AI: "+move)
        else:
            print("Error in AI!")
        b.print_board()
    elif choice2==3:
        resunmv=b.undo_move()
        if(resunmv==False):
            print("Undo Failed!")
        else:
            b.print_board()
    elif choice2==4:
        curr_fen=b.get_fen()
        print("FEN of Current Game State: ",curr_fen)
    elif choice2==5:
        new_fen=str(input("Enter FEN: "))
        b.load_fen(new_fen)
        b.print_board()

