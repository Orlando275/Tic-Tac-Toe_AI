import json
import torch


symbol_to_num = {
    "": 0,
    "X": 1,
    "O": -1
}

result_to_label = {
    "X_wins": 1,
    "O_wins": -1,
    "tie": 0
}

def load_json(path):
    with open(path, "r") as f:
        return json.load(f)

def board_to_tensor(board):
    return torch.tensor([[symbol_to_num[cell] for cell in row] for row in board], dtype=torch.float32)

def move_to_index(move):
    row, col = move
    return row * 3 + col 

def process_data(json_data):
    board_tensors = []
    move_indices = []
    results = []

    for game in json_data:
        result = result_to_label.get(game["result"], 0)
        for move in game["moves"]:
            board = board_to_tensor(move["board"])
            move_index = move_to_index(move["move"])
            board_tensors.append(board)
            move_indices.append(move_index)
           

    return {
        "boards": torch.stack(board_tensors),       
        "moves": torch.tensor(move_indices),        
        "results": torch.tensor(results)            
    }


if __name__ == "__main__":
    json_path = "data_train.json"  
    dataset = load_json(json_path)
    data = process_data(dataset)
    torch.save(data, "tictactoe_dataset.pt")
    print("Dataset saved as tictactoe_dataset.pt")
