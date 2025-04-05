# Maze Solver with Pygame 🧩

This project generates a random maze and uses a recursive Depth-First Search (DFS) algorithm to find a path from a starting point to a destination. The entire process is visualized using Pygame.

## 🔍 Features

- Randomly generated maze grid
- Recursive DFS-based pathfinding algorithm
- Visual representation of the maze and path using Pygame
- Color-coded cells for walls, paths, start, and destination

## 🎮 How It Works

- The maze is a grid of cells where:
  - `-1` represents walls (green)
  - `0` represents empty cells (black)
  - `1` and above are cells visited during the search (orange)
- The algorithm starts from a random empty cell and searches for a destination by recursively visiting neighboring cells.
- The result is drawn on the screen in real time.

## 🧠 Technologies Used

- **Python 3**
- **Pygame**
- **NumPy**

## 🛠️ Installation

1. Make sure you have Python 3 installed.
2. Install dependencies:

   ```bash
   pip install -r requirements.txt
