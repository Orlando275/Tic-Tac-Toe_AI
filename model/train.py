import torch
import torch.nn as nn
import torch.optim as opt
from load_data import load_dataset_TicTacToe
from model import modelTicTacToe

def train():
    model=modelTicTacToe()
    dataset=load_dataset_TicTacToe()
    loss_fn=nn.CrossEntropyLoss()
    optimizer=opt.Adam(params=model.parameters(),lr=0.01)

    
    model.train()
    for epoch in range(10):
        total_loss=0
        for xBatch,yBatch in dataset:
            output=model(xBatch)
            loss=loss_fn(output,yBatch)

            optimizer.zero_grad()
            loss.backward()
            optimizer.step()

            total_loss += loss.item()
    
        print(f"Epoch {epoch+1} - Loss: {total_loss:.4f}")


    correct=0
    total=0

    with torch.no_grad():
        for images,labels in dataset:
            output=model(images)
            predictions=output.argmax(dim=1)
            correct+=(predictions==labels).sum().item()
            total+=labels.size(0)

    print(f"porcentaje de efectividad {100*correct/total:.2f}%")
    torch.save(model.state_dict(),"model_TicTacToe.pth")
if __name__== "__main__":
    train()