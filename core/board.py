import chess

class Board:
    def __init__(self, fen=None):
        if(fen):
            self.board=chess.Board(fen)
        else:
            self.board=chess.Board()

    def print_board(self):
        print(self.board)

    def make_move(self,uci):
        try:
            move=chess.Move.from_uci(uci)
        except chess.InvalidMoveError:
            print("Invalid! Please Enter correct UCI string.")
        if(move in self.board.legal_moves):
            self.board.push(move)
            print("Legal Move")
        else:
            print("Illegal Move")
        
            
    def undo_move(self):
        try:
            self.board.pop()
            print("Successful Undo Operation Performed!")
        except IndexError:
            print("No chess history exists! Play a move first.")

    def get_fen(self):
        return self.board.fen()
    
    def load_fen(self,fen):
        self.board=chess.Board(fen)
        

"""


    

    
        print(Board1.move_stack)


"""