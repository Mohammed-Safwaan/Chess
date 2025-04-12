# Chess
# Chess Game using Pygame  
#### Video Demo: <https://youtu.be/RjQ98caC_78>  
#### Description:

Hello! My name is **Mohammed Safwaan Pasha** from **India**, and this is my final project submission for **CS50**. The project is a fully functional **2-player chess game** built using **Python and the Pygame library**. This chess game replicates the classic board game experience on the computer, featuring turn-based moves, move validation, checkmate detection, move history logging, undo functionality, a timer for each player, and additional visual effects to enhance the gaming experience.

---

## About the Project:

I wanted to challenge myself with a project that combined logic, a graphical user interface, and gameplay mechanics — and chess felt like the perfect fit. Chess is a game of immense complexity and strategy, and creating a digital version requires carefully handling a variety of gameplay rules, user inputs, and graphical elements.

This game was created entirely in **Python** using the **Pygame** library for the graphical interface and event handling. It runs as a standalone desktop application and allows two players to play against each other on the same machine.

---

## Features:

- **Fully Functional Chess Board**: An 8x8 grid rendered with alternating colors, supporting all standard chess moves.
- **Player Turn Handling**: Alternating turns between White and Black.
- **Move Validation**: Ensures only legal moves for each piece are allowed.
- **Checkmate Detection**: Detects when a player is in checkmate and declares the winner.
- **Move History Logging**: Keeps track of each move made during the game.
- **Undo Move Feature**: Allows players to undo their last move.
- **Move Highlighting**: Highlights the selected piece and its possible moves.
- **Timers**: Displays a running timer for each player.
- **Sound Effects**: Play sounds for moves and captures (planned for future implementation).
- **Home Screen**: Players can enter their names before starting a new game.
- **User-friendly Interface**: Clean and intuitive design using Pygame’s surface blitting and event loops.

---

## Project Structure:

- `main.py` : This is the main driver file that initializes the game, runs the game loop, handles player inputs, and manages game state transitions.
- `chess_engine.py` : Contains the core game logic, including move validation, move generation, check and checkmate detection, and tracking move history.
- `images/` : Folder containing image assets for each chess piece (White and Black pieces for King, Queen, Bishop, Knight, Rook, and Pawn).
- `sounds/` : (Optional/Planned) Directory for adding sound effect files for moves, captures, and game over notifications.
- `README.md` : This documentation file explaining the entire project, its features, and file structures.
- `video.mp4` : (Uploaded separately) A video demo showcasing the gameplay and project highlights.

---

## Design Choices and Challenges:

One of the key decisions I made early in the project was to preserve the classic chess mechanics and visuals while focusing on 2-player functionality without AI opponents. This allowed me to focus on perfecting move validation, turn logic, and GUI interactions.

Implementing **checkmate detection** was particularly challenging, as it required iterating through all possible legal moves for a player and checking if any move could remove the player from check. I structured this using a recursive-like move generation and validation function inside the `chess_engine.py`.

Adding the **undo feature** was another interesting part, involving maintaining a move history stack and rolling back moves while restoring game states.

I also chose **Pygame** because it is beginner-friendly yet powerful enough to handle custom GUIs and real-time interaction, perfect for game development projects like this.

---

## Future Improvements:

- Adding **sound effects** for moves, captures, and checkmate announcements.
- Implementing **AI opponent functionality** using the Minimax algorithm.
- Adding options for **game save and load**.
- A proper **pause menu** and enhanced **game-over screen**.
- Online multiplayer capability via sockets.

---

## About Me:

- **Name**: Mohammed Safwaan Pasha  
- **Country**: India  
- **GitHub**: [Mohammed-Safwaan](https://github.com/Mohammed-Safwaan)  
- **edX Account**: safwaan110  

---

## How to Run the Project:

1. Install Python 3.x and Pygame:
    ```bash
    pip install pygame
    ```
2. Clone or download this repository.
3. Place the image assets in the `images/` directory.
4. Run the game using:
    ```bash
    python main.py
    ```

---

## Conclusion:

This project helped me deepen my understanding of object-oriented programming, event-driven applications, and game logic. It was a rewarding learning experience combining logic, visual design, and real-time interaction handling.

I’m proud of how this project turned out and excited to improve it further in the future!

