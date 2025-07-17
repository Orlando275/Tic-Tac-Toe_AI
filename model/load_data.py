import torch
from torch.utils.data import TensorDataset,DataLoader

def load_dataset_TicTacToe():
    data=torch.load("/home/orlandoflorescastillo/Documentos/gatoIA/data/tictactoe_dataset.pt")
    boards=data["boards"]
    moves=data["moves"]
    
    x=boards.view(-1,9).float()
    y=moves.long()
    
    dataset=TensorDataset(x,y)
    loader=DataLoader(dataset=dataset,batch_size=32,shuffle=True)
    return loader
