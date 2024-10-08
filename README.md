﻿# Sudoku Solver and Generator

This project is a comprehensive tool to solve and generate Sudoku puzzles. It includes a graphical user interface (GUI) powered by Tkinter and provides functionalities to solve given Sudoku puzzles, generate new puzzles, and toggle dark mode for better visibility. The application can also save and load configurations.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Functions](#functions)
- [Attributes](#attributes)
- [Configuration](#configuration)

## Features

- Solve Sudoku puzzles.
- Generate new Sudoku puzzles.
- Toggle dark mode.
- Save and load configuration settings.
- Interactive GUI built with Tkinter.

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/sudoku-solver-generator.git
    ```
2. Navigate to the project directory:
    ```bash
    cd sudoku-solver-generator
    ```
3. Install the required dependencies using `pip`:
    ```bash
    pip install tk customtkinter
    ```

## Functions

- `solve_sudoku(board)`: Attempts to solve the Sudoku puzzle using backtracking algorithm.
- `find_empty(board)`: Finds an empty cell in the Sudoku board.
- `is_safe(board, num, pos)`: Checks if a number can be placed at a given position.
- `generate_sudoku(difficulty)`: Generates a new Sudoku puzzle with a specific difficulty level.
- `load_config()`: Loads the user configuration from a file.
- `save_config()`: Saves the user configuration to a file.
- `configure_dark_mode()`: Configures the application for dark mode.
- `toggle_dark_mode()`: Toggles dark mode on or off.
- `solve()`: Handles solving the Sudoku puzzle from the GUI.
- `generate()`: Handles generating a new Sudoku puzzle from the GUI.
- `issolved()`: Checks if the current Sudoku puzzle is solved from the GUI.

## Attributes

- `tk`: Main Tkinter module for GUI.
- `ctk`: Custom Tkinter module for theming.
- `CONFIG_FILE`: Path to the configuration file.
- `root`: Main window of the application.
- `board_cells`: 2D array representing the Sudoku board cells in the GUI.
- `_`: Placeholder attribute.
- `row`: Represents rows in the Sudoku board.
- `col`: Represents columns in the Sudoku board.
- `padx`: Horizontal padding for GUI components.
- `pady`: Vertical padding for GUI components.
- `solve_button`: Button in the GUI for solving Sudoku.
- `generate_button`: Button in the GUI for generating new Sudoku puzzles.
- `issolved_button`: Button in the GUI for checking if the Sudoku is solved.
- `config`: User configuration settings.
- `menu_bar`: Menu bar in the GUI.
- `options_menu`: Options menu in the GUI.

## Configuration

The configuration settings are stored in a file specified by `CONFIG_FILE`. The settings include user preferences like dark mode. These settings can be loaded and saved using the functions `load_config()` and `save_config()`.

---

Enjoy solving and generating Sudoku puzzles with this tool!
