# Project Ideas
**Tic-Tac-Toe AI Trainer** is a Python-based game where you can:
- Play **Player vs Player** Tic-Tac-Toe and save games.
- **Train a custom AI model** to improve over time based on past games.

---

## Installation & Setup

### Clone this repository
```bash
git clone https://github.com/Orlando275/Tic-Tac-Toe_AI
```

### Activate virtual enviroment python 
```bash
# On Linux / Mac
source venv/bin/activate
# On Windows (PowerShell)
venv\Scripts\Activate.ps1
```

### Start playing
```bash
cd game
python -m game.play_tic_tac_toe
```

---

## Docker Image

You can pull and run the latest version of the TicTacToe AI from Docker Hub:

```bash
docker pull orlando2705/tictactoeai:latest
docker run -it --rm orlando2705/tictactoeai:latest
```

---

## Features
- **PvP Mode** – Play with a friend on the same machine.
- **Match History Saving** – Every game is stored for future analysis and training.
- **AI Training Module** – The AI improves by learning from stored games.

---

## Project Structure
<pre>
Tic-Tac-Toe_AI/
├── data/
│   ├── data_train.json
│   ├── jsonToTensor.py
│   └── tictactoe_dataset.pt
├── game/
│   ├── logic.py
│   └── play_tic_tac_toe.py
├── model/
│   ├── load_data.py
│   ├── model_TicTacToe.pth
│   ├── model.py
│   └── train.py
├── utils/
│   └── paths.py
├── .gitignore
├── Dockerfile
├── README.md
└── requirements.txt
</pre>
---

## Screenshots

### Gameplay
![Game in progress](https://github.com/user-attachments/assets/8328278b-aadf-4180-bfe7-40198af31f34)

### Game endscreen
![Game end screen](https://github.com/user-attachments/assets/e291aed6-b898-4ec7-becd-a5bccb8e4610)

### AI training output
![AI training output](https://github.com/user-attachments/assets/4f65e74b-eb56-4688-981a-85f42d4b03f3)

---

## How It Works

- **Game Execution**: The game launches from `main.py` and prompts for Player 1 and Player 2 moves.
- **Data Storage**: Every move and match result is saved in `/data` as a structured file for training.
- **AI Training**: The saved game moves are used to train the AI, improving its decision-making abilities.
- **Real-Time Inference**: The game uses a previously trained model to make predictions and play in real time.

---

### License
This project is licensed under the MIT License – see the [LICENSE](LICENSE) file for details.
