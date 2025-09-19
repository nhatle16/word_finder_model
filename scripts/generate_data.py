from typing import List, Tuple

import random
import string

# Defined a fixed size (10 x 10) for the word grid
SIZE = 10

# Define possible directions
DIRECTIONS = [
    (0, 1),   # right
    (1, 0),   # down
    (1, 1),   # diagonal down-right
    (0, -1),  # left
    (-1, 0),  # up
    (-1, -1), # diagonal up-left
    (1, -1),  # diagonal down-left
    (-1, 1)   # diagonal up-right
]

# Simple word list
WORD_LIST = ["python", "java", "kotlin", "ruby", "swift", "go", "rust", "scala", "perl"]

def place_word(grid: List[List[str]], word: str) -> Tuple[int, int, int, int]:
    n = len(grid)
    attempts = 100

    while attempts > 0:
        dx, dy = random.choice(DIRECTIONS)

        # Choose a random starting point
        x = random.randint(0, n - 1)
        y = random.randint(0, n - 1)

        # Find the ending point
        end_x = x + dx * (len(word) - 1)
        end_y = y + dy * (len(word) - 1)

        # Check if the word fits in the grid, then try to place it
        if 0 <= end_x < n and 0 <= end_y < n:
            possible = True
            for i, char in enumerate(word):
                # Get coordinates for the current character
                new_x = x + dx * i
                new_y = y + dy * i
                # Validate placement
                if grid[new_x][new_y] not in ('', char):
                    possible = False
                    break

            if possible:
                for i, char in enumerate(word):
                    new_x = x + dx * i
                    new_y = y + dy * i
                    grid[new_x][new_y] = char
                
                # Return the coordinates and direction of the placed word
                return (x, y, dx, dy)
        attempts -= 1
    return None

def generate_grid(n: int, words: List[str]) -> Tuple[List[List[str]], List[Tuple[str, Tuple[int, int, int, int]]]]:
    grid = [['' for _ in range(n)] for _ in range(n)]
    labels = []

    # Place each word in the grid
    for word in words:
        pos = place_word(grid, word)
        if pos:
            labels.append((word, pos))

    # Place random letters in empty cells
    for y in range(n):
        for x in range(n):
            if grid[y][x] == '':
                grid[y][x] = random.choice(string.ascii_lowercase)
    return grid, labels

def search_word(grid: List[List[str]], label: Tuple[str, Tuple[int, int, int, int]]) -> None:
    if not label or not label[1]:
        return None

    n = len(grid)
    word = label[0]
    x, y, dx, dy = label[1]
    
    for i, ch in enumerate(word):
        new_x = x + dx * i
        new_y = y + dy * i
        grid[new_x][new_y] = ch.upper()

if __name__ == "__main__":
    grid, labels = generate_grid(n=SIZE, words=WORD_LIST)
    for label in labels:
        search_word(grid, label)

    for r in grid:
        for char in r:
            print(char, end=' ')
        print()