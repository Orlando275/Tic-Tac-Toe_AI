<!-- Banner -->
<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=rect&color=gradient&height=100&section=header&text=Tic-Tac-Toe%20AI%20Trainer&fontSize=40&animation=fadeIn" />
</p>

## 🎯 Project Overview
**Tic-Tac-Toe AI Trainer** is a Python-based game where you can:
- Play **Player vs Player** Tic-Tac-Toe.
- **Save match history** for later analysis.
- **Train a custom AI model** to improve over time based on past games.

This project is designed to showcase **game logic implementation**, **data persistence**, and **basic AI training workflows** — all in a simple, interactive environment.

---

## 📥 Installation & Setup

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

## 🐳 Docker Image

You can pull and run the latest version of the TicTacToe AI from Docker Hub:

```bash
docker pull orlando2705/tictactoeai:version2.0
docker run -it --rm orlando2705/tictactoeai:version2.0
```

---

## ✨ Features
- 👫 **PvP Mode** – Play with a friend on the same machine.
- 💾 **Match History Saving** – Every game is stored for future analysis and training.
- 🧠 **AI Training Module** – The AI improves by learning from stored games.
- 🎯 **Replay & Analysis** – Inspect past games to understand AI decisions.
- 🔄 **Modular Design** – Easy to expand with new features or game variations.

---

## 📂 Project Structure
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

## 🖼️ Screenshots

### Game in progress
![Game in progress](https://github.com/user-attachments/assets/8328278b-aadf-4180-bfe7-40198af31f34)

### Game end screen
![Game end screen](https://github.com/user-attachments/assets/e291aed6-b898-4ec7-becd-a5bccb8e4610)

### AI training output
![AI training output](https://github.com/user-attachments/assets/4f65e74b-eb56-4688-981a-85f42d4b03f3)

---

## 🎯 How It Works

- **Game Execution**: The game launches from `main.py` and prompts for Player 1 and Player 2 moves.
- **Data Storage**: Every move and match result is saved in `/data` as a structured file for training.
- **AI Training**: The AI reads past games and adjusts its decision-making algorithm accordingly.
- **Replay Analysis**: Past games can be reviewed to understand AI strategy changes.

## 🛠 Technologies Used
- Python 3
- Framework Pytorch
- JSON – Data persistence
- Basic Machine Learning concepts – Custom AI training loop

## 🚀 Future Improvements
- Add AI vs Player mode in real-time
- Implement a Tkinter interface 
- Visualize AI decision-making with heatmaps
- Add Docker support for easy deployment

---

## 📄 License
This project is licensed under the MIT License – see the [LICENSE](LICENSE) file for details.
