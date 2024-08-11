# Tic-Tac-Toe-AI

![tictac](https://github.com/user-attachments/assets/340ca678-5c79-4519-b9e2-64ee515a7e59)
  

This is a simple Tic Tac Toe game implemented using Python and Pygame. The game features a player vs. computer mode where the player is 'X' and the computer is 'O'.

## Features

- **Player vs. Computer**: The game allows you to play against the computer. The computer uses a minimax algorithm to make optimal moves.
- **Interactive UI**: The game uses Pygame to create a visually appealing and interactive user interface.
- **Win Detection**: The game automatically detects when a player wins or if there's a tie, and displays the result.
- **Dark Theme**: The game features a dark, iOS-themed color scheme for an aesthetically pleasing experience.

## Requirements

- Python 3.x
- Pygame (`pip install pygame`)

## How to Play

1. Clone the repository or copy the code into a Python script.
2. Make sure you have Pygame installed. You can install it using pip:

    ```bash
    pip install pygame
    ```
3. Run the script:

    ```bash
    python tic_tac_toe.py
    ```
4. The game window will open. Click on the grid to place your 'X'. The computer will automatically place an 'O' after your move.
5. The game will detect when a player wins or if there's a tie, and display the result.

## Code Overview

- **Main Variables:**
  - `WIDTH`, `HEIGHT`: The dimensions of the game window.
  - `LINE_WIDTH`, `CIRCLE_RADIUS`, `CIRCLE_WIDTH`, `CROSS_WIDTH`, `SPACE`: Various dimensions and spacings for the board and figures.
  - `BG_COLOR`, `LINE_COLOR`, `CIRCLE_COLOR`, `CROSS_COLOR`: Colors used in the game.

- **Functions:**
  - `draw_lines()`: Draws the grid lines on the board.
  - `draw_figures()`: Draws the circles and crosses on the board.
  - `mark_square(row, col, player)`: Marks the given square with the player's symbol.
  - `available_square(row, col)`: Checks if a square is available.
  - `is_board_full()`: Checks if the board is full.
  - `check_win_and_drawlines(player)`: Checks if a player has won and draws the winning line.
  - `check_win(player)`: Checks if a player has won.
  - `endgame(running)`: Handles endgame scenarios like win or tie.
  - `minimax(board, ismaxi)`: Implements the minimax algorithm for the computer's AI.
  - `computer_turn()`: Handles the computer's move.

## License

This project is open source and available under the [MIT License](LICENSE).
