# Jeu Taquin Solver

This project implements a solution for the "Jeu Taquin" (also known as the 8-puzzle or sliding puzzle) using various search algorithms. The goal of the puzzle is to rearrange tiles on a 3x3 grid to match a predefined final state by sliding tiles into an empty space.

## Features

- **Initial and Final States**:
  - Defines the initial state of the puzzle and checks if a given state matches the final state.

- **State Manipulation**:
  - Identifies the position of the empty tile.
  - Performs tile swaps to generate new states.

- **State Display**:
  - Provides a visual representation of the puzzle grid.

- **State Transitions**:
  - Generates all possible states from a given state by moving the empty tile.

- **Search Algorithms**:
  - **Breadth-First Search (BFS)**: Explores all states level by level to find the solution.
  - **Depth-Limited Search (DLS)**: Searches for a solution up to a specified depth limit.
  - **A* Search**: Uses a heuristic function to prioritize states based on their distance from the final state.

- **Heuristic Function**:
  - Calculates the number of misplaced tiles compared to the final state.

## Example

The initial state is:
1 2 3 8 6 0 7 5 4

The program attempts to solve the puzzle using the implemented algorithms and displays the solution process.

## How to Run

1. Clone the repository:
   ```sh
   git clone https://github.com/your-username/jeu-taquin-solver.git
   cd jeu-taquin-solver
Run the Python script:
python "projet IA Jeu taquin.py"
The program will execute the following algorithms:

Depth-Limited Search
Breadth-First Search
A* Search
The results, including the steps taken and time spent, will be displayed in the console.

Requirements
Python 3.x
No additional libraries are required.
File Structure
IA-Project-jeu-taquin-master/
├── projet IA Jeu taquin.py  # Main script implementing the puzzle solver
License
This project is licensed under the MIT License. See the LICENSE file for details.

Acknowledgments
This project is a practical demonstration of AI search techniques applied to a classic problem, making it a useful resource for learning about problem-solving in artificial intelligence.

