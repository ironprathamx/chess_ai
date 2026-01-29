import chess

is_fen = bool(input("Do you want to import a FEN?:"))
if(is_fen):
    fen=str(input("Enter fen: "))
    Board1=chess.Board(fen)
else:
    Board1=chess.Board()
print(Board1)
while(1):
    print(Board1)
    try:
        string=str(input("Enter your move: "))
        try:
            if (string=="undo"):
                Board1.pop()
                print("Successful Undo Operation Performed!")
                continue
        except IndexError:
            print("No chess history exists! Play a move first.")
            continue
        if(string=="get_fen"):
            b1_fen=Board1.fen()
            print("FEN aquired in b1_fen variable!")
            continue
        move=chess.Move.from_uci(string)

    except chess.InvalidMoveError:
        print("Invalid! Please Enter correct UCI string.")
        continue

    if(move in Board1.legal_moves):
        Board1.push(move)
        print("Legal Move")

    else:
        print("Illegal Move")
        print(Board1.move_stack)


