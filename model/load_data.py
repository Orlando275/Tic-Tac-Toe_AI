import torch
from torch.utils.data import TensorDataset,DataLoader
from utils import paths

def load_dataset_TicTacToe():
    path_dataset=paths.get_dataset_path()
    data=torch.load(path_dataset)
    boards=data["boards"]
    moves=data["moves"]
    
    x=boards.view(-1,9).float()
    y=moves.long()
    
    dataset=TensorDataset(x,y)
    loader=DataLoader(dataset=dataset,batch_size=32,shuffle=True)
    return loader
