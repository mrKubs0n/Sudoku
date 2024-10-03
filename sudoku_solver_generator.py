import tkinter as tk
from tkinter import messagebox, Menu
import customtkinter as ctk
import json
import os

CONFIG_FILE = "config.json"


def solve_sudoku(grid):
    empty = find_empty(grid)
    if not empty:
        return True
    row, col = empty

    for i in range(1, 10):
        if is_safe(grid, row, col, i):
            grid[row][col] = i
            if solve_sudoku(grid):
                return True
            grid[row][col] = 0
    return False


def find_empty(grid):
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 0:
                return (i, j)
    return None


def is_safe(grid, row, col, num):
    box_row = row - row % 3
    box_col = col - col % 3

    if num in grid[row] or num in [grid[i][col] for i in range(9)]:
        return False

    for i in range(3):
        for j in range(3):
            if grid[box_row + i][box_col + j] == num:
                return False

    return True


def generate_sudoku():
    import random
    grid = [[0] * 9 for _ in range(9)]
    for _ in range(17):
        row = random.randint(0, 8)
        col = random.randint(0, 8)
        num = random.randint(1, 9)
        if is_safe(grid, row, col, num):
            grid[row][col] = num
    return grid


def load_config():
    if not os.path.exists(CONFIG_FILE):
        return {"dark_mode": True}
    with open(CONFIG_FILE, "r") as f:
        return json.load(f)


def save_config(config):
    with open(CONFIG_FILE, "w") as f:
        json.dump(config, f)


def configure_dark_mode(state):
    mode = "dark" if state else "light"
    ctk.set_appearance_mode(mode)
    dark_bg = "#2e2e2e" if state else "white"
    dark_fg = "#ffffff" if state else "black"
    for row in range(9):
        for col in range(9):
            board_cells[row][col].configure(bg=dark_bg, fg=dark_fg, insertbackground=dark_fg)
    solve_button.configure(fg_color=dark_bg, text_color=dark_fg)
    generate_button.configure(fg_color=dark_bg, text_color=dark_fg)
    issolved_button.configure(fg_color=dark_bg, text_color=dark_fg)
    # options_menu.configure(fg_color=dark_bg,text_color=dark_fg)


def toggle_dark_mode():
    config['dark_mode'] = not config['dark_mode']
    configure_dark_mode(config['dark_mode'])
    save_config(config)


def solve():
    grid = [[int(board_cells[row][col].get() or 0) for col in range(9)] for row in range(9)]
    if solve_sudoku(grid):
        for row in range(9):
            for col in range(9):
                board_cells[row][col].delete(0, tk.END)
                board_cells[row][col].insert(0, grid[row][col])
    else:
        messagebox.showerror("Error", "No solution found")


def generate():
    grid = generate_sudoku()
    for row in range(9):
        for col in range(9):
            color = "#2e2e2e" if config['dark_mode'] else "white"
            board_cells[row][col].configure(bg=color)
            board_cells[row][col].delete(0, tk.END)
            if grid[row][col] != 0:
                board_cells[row][col].insert(0, grid[row][col])


def issolved():
    guard = False
    grid = [[int(board_cells[row][col].get() or 0) for col in range(9)] for row in range(9)]
    for num in range(1, 10):
        for row in range(9):
            for col in range(9):
                if is_safe(grid, row, col, num):
                    guard = True
                    board_cells[row][col].configure(bg='red')

    if not guard:
        messagebox.showinfo("Solved", "Sudoku is solved, GJ M8")
    else:
        for row in range(9):
            for col in range(9):
                if board_cells[row][col].get() == '0':
                    color = "#2e2e2e" if config['dark_mode'] else "white"
                    board_cells[row][col].configure(bg=color)


ctk.set_appearance_mode("dark")
root = ctk.CTk()
root.title("Sudoku Solver & Generator")
root.resizable(False,False)

board_cells = [
    [tk.Entry(root, width=2, font=("Arial Black", 27), borderwidth=2, relief="solid", justify="center") for _ in
     range(9)]
    for _ in range(9)
]

for row in range(9):
    for col in range(9):
        if (col + 1) % 3 == 0 and col != 8:
            padx = (0, 10)
        else:
            padx = (0, 2)
        if (row + 1) % 3 == 0 and row != 8:
            pady = (0, 10)
        else:
            pady = (0, 2)
        board_cells[row][col].grid(row=row, column=col, padx=padx, pady=pady)

solve_button = ctk.CTkButton(root, text="Solve", command=solve)
solve_button.grid(row=10, column=0, columnspan=9, pady=10, sticky="ew")

generate_button = ctk.CTkButton(root, text="Generate", command=generate)
generate_button.grid(row=11, column=0, columnspan=9, pady=10, sticky="ew")

issolved_button = ctk.CTkButton(root, text="Look for mistakes", command=issolved)
issolved_button.grid(row=12, column=0, columnspan=9, pady=10, sticky="ew")

config = load_config()
configure_dark_mode(config['dark_mode'])

menu_bar = Menu(root)
options_menu = Menu(menu_bar, tearoff=0)
options_menu.add_command(label="Going Dark?", command=toggle_dark_mode)
menu_bar.add_cascade(label="Options", menu=options_menu)
root.config(menu=menu_bar)

root.mainloop()