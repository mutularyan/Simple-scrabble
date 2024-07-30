import random
from collections import Counter

print("WELCOME TO SCRABBLE, GOOD LUCK")

def load_dictionary(file_path):
    with open(file_path, 'r') as file:
        words = file.read().splitlines()
    return [word.upper() for word in words]

dictionary = load_dictionary(r'C:\Users\LENOVO\Desktop\Simple scrabble project\Simple-scrabble\dictionary.txt')

board = [[" " for _ in range(15)] for _ in range(15)]
special_tiles = {
    (8, 8): "  X ", (1, 1): " TW ", (1, 4): " DL ", (1, 8): " TW ", (1, 12): " DL ", (1, 15): " TW ",
    (2, 2): " DW ", (2, 6): " TL ", (2, 10): " TL ", (2, 14): " DW ", (3, 3): " DL ", (3, 7): " DL",
    (3, 9): " DL ", (3, 13): " DW ", (4, 1): " DL ", (4, 4): " DW ", (4, 8): " DL ", (4, 12): " DW ",
    (4, 15): " DL ", (5, 5): " DW ", (5, 11): " DW ", (6, 2): " TL ", (6, 6): " TL ", (6, 10): " TL ",
    (6, 14): " TL ", (7, 3): " DL", (7, 7): " DL ", (7, 9): " DL ", (7, 13): " DL ", (8, 1): " TW ",
    (8, 4): " DL ", (8, 12): " DL ", (8, 15): " TW ", (9, 3): " DL ", (9, 7): " DL ", (9, 9): " DL ",
    (9, 13): " DL ", (10, 2): " TL ", (10, 6): " TL ", (10, 10): " TL", (10, 14): " TL ", (11, 5): " DW ",
    (11, 11): " DW ", (12, 1): " DL ", (12, 4): " DW ", (12, 8): " DL ", (12, 12): " DW ", (12, 15): " DL ",
    (13, 3): " DW ", (13, 7): " DL ", (13, 9): " DL ", (13, 13): " DW ", (14, 2): " DW ", (14, 6): " TL",
    (14, 10): " TL ", (14, 14): " DW ", (15, 1): " TW ", (15, 4): " DL", (15, 8): " TW ", (15, 12): " DL ",
    (15, 15): " TW "
}

for (row, col), tile in special_tiles.items():
    board[row][col] = tile

letter_points = {
    'A': 1, 'B': 3, 'C': 3, 'D': 2, 'E': 1,
    'F': 4, 'G': 2, 'H': 4, 'I': 1, 'J': 8,
    'K': 5, 'L': 1, 'M': 3, 'N': 1, 'O': 1,
    'P': 3, 'Q': 10, 'R': 1, 'S': 1, 'T': 1,
    'U': 1, 'V': 4, 'W': 4, 'X': 8, 'Y': 4, 'Z': 10
}

letter_no = {
    'A': 9, 'B': 2, 'C': 2, 'D': 4, 'E': 12,
    'F': 2, 'G': 3, 'H': 2, 'I': 9, 'J': 1,
    'K': 1, 'L': 4, 'M': 2, 'N': 6, 'O': 8,
    'P': 2, 'Q': 1, 'R': 6, 'S': 4, 'T': 6,
    'U': 4, 'V': 2, 'W': 2, 'X': 1, 'Y': 2, 'Z': 1
}
letter_bag = []

for letter, count in letter_no.items():
    letter_bag.extend([letter] * count)
random.shuffle(letter_bag)
player_rack = [letter_bag.pop() for _ in range(7)]
computer_rack = [letter_bag.pop() for _ in range(7)]

def display_board():
    cell_width = 4

    header = "     " + " | ".join(f"{i:<{cell_width}}" for i in range(15)) + " |"
    separator = "  " + "+".join("-" * (cell_width + 2) for _ in range(15)) + "+"

    board_str = header + "\n" + separator + "\n"

    for i in range(15):
        row_header = f"{i:<2} | "
        row_content = " | ".join(f"{board[i][j]:<{cell_width}}" for j in range(15))
        row_str = row_header + row_content + " |"

        board_str += row_str + "\n"
        board_str += separator + "\n"

    print(board_str)

def can_form_word(word, rack):
    rack_counter = Counter(rack)
    word_counter = Counter(word)
    for letter, count in word_counter.items():
        if rack_counter[letter] < count:
            return False
    return True

def calculate_score(word, row, col, direction):
    word_score = 1
    score = 0
    
    for i, letter in enumerate(word):
        current_row, current_col = (row, col + i) if direction == 'H' else (row + i, col)
        letter_score = letter_points[letter]
        
        if (current_row, current_col) in special_tiles:
            tile = special_tiles[(current_row, current_col)].strip()
            if tile == "DL":
                letter_score *= 2
            elif tile == "TL":
                letter_score *= 3
            elif tile == "DW":
                word_score *= 2
            elif tile == "TW":
                word_score *= 3

        score += letter_score
    
    return score * word_score

def play_word(rack, is_computer=False):
    display_board()
    if is_computer:
        print(f"Computer's rack: {rack}")
        valid_words = [word for word in dictionary if can_form_word(word, rack)]
        if not valid_words:
            print("Computer has no valid words.")
            return 0
        word = random.choice(valid_words)
        row, col, direction = random.randint(0, 14), random.randint(0, 14), random.choice(['H', 'V'])
    else:
        print(f"Your rack: {rack}")
        word = input("Enter the word you want to play (from your rack): ").strip().upper()
        row = int(input("Enter the row number (0-14): ").strip())
        col = int(input("Enter the column number (0-14): ").strip())
        direction = input("Enter direction (H for horizontal, V for vertical): ").strip().upper()

    if all(letter in rack for letter in word):
        if direction == 'H' and col + len(word) <= 15:
            for i, letter in enumerate(word):
                board[row][col + i] = letter
                rack.remove(letter)
        elif direction == 'V' and row + len(word) <= 15:
            for i, letter in enumerate(word):
                board[row + i][col] = letter
                rack.remove(letter)
        else:
            print("Invalid move. Word does not fit on the board.")
            return 0
        
        score = calculate_score(word, row, col, direction)
        print(f"Word played: {word}, Score: {score}")
        return score
    else:
        print("You don't have the letters to play this word. Kindly try again.")
        return 0

def draw_tiles(rack):
    while len(rack) < 7 and letter_bag:
        rack.append(letter_bag.pop())

def game_loop():
    player_score = 0
    computer_score = 0

    while letter_bag:
        print("\nPlayer's turn")
        player_score += play_word(player_rack)
        draw_tiles(player_rack)

        print("\nComputer's turn")
        computer_score += play_word(computer_rack, is_computer=True)
        draw_tiles(computer_rack)

        print(f"\nPlayer score: {player_score}")
        print(f"Computer score: {computer_score}")

        if not letter_bag:
            break
    
    if player_score > computer_score:
        print("YOU WIN! A HUGE CONGRATULATIONS!")
    else:
        print("THE COMPUTER WINS! TRY BETTER NEXT TIME!")

game_loop()
