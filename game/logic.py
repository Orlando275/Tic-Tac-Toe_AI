import json
import os
import copy
from utils import paths

class GameLogic:
    def __init__(self):
        self.history = []
        self.count = 0
        self.symbol = "X"
        self.board = [["" for _ in range(3)] for _ in range(3)]

    def reset(self):
        self.count = 0
        self.symbol = "X"
        self.board = [["" for _ in range(3)] for _ in range(3)]
        self.history.clear()

    def make_move(self, row, col):
        if self.board[row][col] != "":
            return False

        self.symbol = "O" if self.count % 2 == 1 else "X"
        self.board[row][col] = self.symbol
        self.count += 1

        self.history.append({
            "board": copy.deepcopy(self.board),
            "player": self.symbol,
            "move": [row, col]
        })

        return True

    def check_winner(self):
        for row in self.board:
            if all(cell == self.symbol for cell in row):
                return True

        for col in range(3):
            count = 0
            for row in range(3):
                if self.board[row][col] == self.symbol:
                    count += 1
            if count == 3:
                return True

        if all(self.board[i][i] == self.symbol for i in range(3)):
            return True

        if all(self.board[i][2 - i] == self.symbol for i in range(3)):
            return True

        return False


    def save_game(self, result):

        game_data = {
            "moves": self.history,
            "result": result
        }
        
        #load path to file json
        path_fileJSON=paths.get_trainJSON_path()
        filename = path_fileJSON

        if os.path.exists(filename):
            with open(filename, "r") as f:
                data = json.load(f)
        else:
            data = []

        data.append(game_data)

        with open(filename, "w") as f:
            json.dump(data, f, indent=4)

        print(f"Game appended to {filename}")
