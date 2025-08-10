import tkinter as tk
import os
import torch
from utils import paths
from game.logic import GameLogic
from model.model import modelGame

class TrainGame:
    def __init__(self):
        self.game_IA=False
        self.logic = GameLogic()
        self.window = tk.Tk()
        self.window.title("Game Tic-Tac-Toe")
        self.window.geometry("700x830")

        self.label_instructions = tk.Label(self.window, text="Select the box and press or press 'a' for playing with AI", font=("Arial", 20), bg="white")
        self.label_instructions.pack(padx=30, pady=20)

        self.label_turn = tk.Label(self.window, text="X goes now", font=("Arial", 15), bg="white")
        self.label_turn.pack(padx=30, pady=0)

        self.canvas = tk.Canvas(self.window, width=600, height=600, bg="white")
        self.canvas.pack(padx=30, pady=50)

        #enable buttons
        self.canvas.bind("<Button-1>", self.click_box)
        self.window.bind("<g>", self.reset_game)
        self.window.bind("<G>", self.reset_game)
        self.window.bind("<A>",self.gameStartAI)
        self.window.bind("<a>",self.gameStartAI)
        
        self.draw_board()

    def gameStartAI(self,event=None):
        self.game_IA=True
        self.symbol_to_number={
            "":0,
            "X":1,
            "O":-1
        }

        #get relative path
        self.path_model = paths.get_model_path()
        if not os.path.exists(self.path_model):
            self.label_instructions.config(text="Model not found. Train it first.")
            self.game_IA = False
            return

        #load model from file
        self.model=modelGame()
        self.model.load_state_dict(torch.load(self.path_model))
        self.model.eval()

        self.label_instructions.config(text="You are playing with AI", font=("Arial", 20), bg="white")
        self.label_turn.config(text="X goes now (human)", font=("Arial", 15), bg="white")
        
        self.canvas.bind("<Button-1>", self.click_box)

    def draw_board(self):
        for i in range(1, 3):
            self.canvas.create_line(i * 200, 0, i * 200, 600)
            self.canvas.create_line(0, i * 200, 600, i * 200)

    def reset_game(self, event=None):
        self.logic.reset()
        self.game_IA = False
        self.canvas.delete("all")
        self.draw_board()
        self.label_turn.config(text="X goes now")
        self.label_instructions.config(text="Select the box and press or press 'a' for playing with AI")

        self.canvas.bind("<Button-1>", self.click_box)
        self.window.bind("<A>",self.gameStartAI)
        self.window.bind("<a>",self.gameStartAI)

    def click_box(self, event):
        self.window.unbind("<A>")
        self.window.unbind("<a>")

        row = int(event.y / 200)
        col = int(event.x / 200)

        if not self.logic.make_move(row, col):
            self.label_turn.config(text="It have already been selected")
            return

        symbol = self.logic.symbol
        self.canvas.create_text((col + 1) * 200 - 100, (row + 1) * 200 - 100,
                                text=symbol, font=("Arial", 100), fill="black")

        if self.logic.check_winner():
            self.label_turn.config(text=f"{symbol} wins!")
            self.label_instructions.config(text="Press 'G' to continue playing")
            self.game_IA=False
            self.canvas.unbind("<Button-1>")
            self.logic.save_game(result=f"{symbol}_wins")
            return
        elif self.logic.count == 9:
            self.label_turn.config(text="It's a tie!")
            self.label_instructions.config(text="Press 'G' to continue playing")
            self.game_IA=False
            self.canvas.unbind("<Button-1>")
            self.logic.save_game(result="tie")
            return

        if self.game_IA:
            self.board_to_tensor()

        else:
            next_symbol = "X" if symbol == "O" else "O"
            self.label_turn.config(text=f"{next_symbol} goes now")

        

    def move_IA(self,row,col):
        symbol = self.logic.symbol
        self.canvas.create_text((col + 1) * 200 - 100, (row + 1) * 200 - 100,
                                text=symbol, font=("Arial", 100), fill="black")

        if self.logic.check_winner():
            self.label_turn.config(text=f"{symbol} wins!")
            self.canvas.unbind("<Button-1>")
            self.logic.save_game(result=f"{symbol}_wins")
        elif self.logic.count == 9:
            self.label_turn.config(text="It's a tie!")
            self.canvas.unbind("<Button-1>")
            self.logic.save_game(result="tie")
        else:
            next_symbol = "X" if symbol == "O" else "O"
            self.label_turn.config(text=f"{next_symbol} goes now")

    def board_to_tensor(self):
        
        #transform board to tensor in view (N,9)
        board=self.logic.board
        board_tensor=torch.tensor([[self.symbol_to_number[cell]for cell in row]for row in board], dtype=torch.float32)
        board_tensor=board_tensor.view(1,-1)
        
        
        
        with torch.no_grad():
            output=self.model(board_tensor).squeeze(0)
            values,index=torch.topk(output,k=9)

        for i in index:
            row=int(i//3)
            col=int(i%3)

            if self.logic.make_move(row,col):
                self.move_IA(row,col)
                return

    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    game = TrainGame()
    game.run()
