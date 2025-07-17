import os

base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__),".."))

def get_model_path(filename="model_TicTacToe.pth"):
    return os.path.join(base_dir,"model",filename)

def get_dataset_path(filename="tictactoe_dataset.pt"):
    return os.path.join(base_dir,"data",filename)

def get_trainJSON_path(filename="data_tarin.json"):
    return os.path.join(base_dir,"data",filename)