import random
from collections import Counter

print("WELCOME TO SCRABBLE, GOOD LUCK")

def load_dictionary(file_path):
    with open(file_path, 'r') as file:
        words = file.read().splitlines()
    return [word.upper() for word in words]

dictionary = load_dictionary('dictionary.txt')

board = [[" " for _ in range(15)] for _ in range(15)]
special_tiles = {
    (7, 7): "  X ", (0, 0): " TW ", (0, 3): " DL ", (0, 7): " TW ", (0, 11): " DL ", (0, 14): " TW ",
    (1, 1): " DW ", (1, 5): " TL ", (1, 9): " TL ", (1, 13): " DW ", (2, 2): " DW ", (2, 6): " DL",
    (2, 8): " DL ", (2, 12): " DW ", (3, 0): " DL ", (3, 3): " DW ", (3, 7): " DL ", (3, 11): " DW ",
    (3, 14): " DL ", (4, 4): " DW ", (4, 10): " DW ", (5, 1): " TL ", (5, 5): " TL ", (5, 9): " TL ",
    (5, 13): " TL ", (6, 2): " DL", (6, 6): " DL ", (6, 8): " DL ", (6, 12): " DL ", (7, 0): " TW ",
    (7, 3): " DL ", (7, 11): " DL ", (7, 14): " TW ", (8, 2): " DL ", (8, 6): " DL ", (8, 8): " DL ",
    (8, 12): " DL ", (9, 1): " TL ", (9, 5): " TL ", (9, 9): " TL", (9, 13): " TL ", (10, 4): " DW ",
    (10, 10): " DW ", (11, 0): " DL ", (11, 3): " DW ", (11, 7): " DL ", (11, 11): " DW ", (11, 14): " DL ",
    (12, 2): " DW ", (12, 6): " DL ", (12, 8): " DL ", (12, 12): " DW ", (13, 1): " DW ", (13, 5): " TL",
    (13, 9): " TL ", (13, 13): " DW ", (14, 0): " TW ", (14, 3): " DL", (14, 7): " TW ", (14, 11): " DL ",
    (14, 14): " TW "
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

def play_word(rack, is_computer=False, is_first_word=False):
    display_board()
    if is_computer:
        print(f"Computer's rack: {rack}")
        valid_words = [word for word in dictionary if can_form_word(word, rack)]
        if not valid_words:
            print("Computer has no valid words.")
            return 0
        word = random.choice(valid_words)
        while True:
            row, col, direction = random.randint(0, 14), random.randint(0, 14), random.choice(['H', 'V'])
            if direction == 'H' and col + len(word) <= 15:
                if all(board[row][col + i] in [" ", word[i]] for i in range(len(word))):
                    break
            elif direction == 'V' and row + len(word) <= 15:
                if all(board[row + i][col] in [" ", word[i]] for i in range(len(word))):
                    break
    else:
        print(f"Your rack: {rack}")
        word = input("Enter the word you want to play(from your rack): ").strip().upper()
        if is_first_word:
            print("First move must be played from the center X!")
            row, col, direction = int(input("Enter the row number (0-14): ").strip()), int(input("Enter the column number (0-14): ").strip()), input("Enter direction (H for horizontal, V for vertical): ").strip().upper()
        else:
            row = int(input("Enter the row number (0-14): ").strip())
            col = int(input("Enter the column number (0-14): ").strip())
            direction = input("Enter direction (H for horizontal, V for vertical): ").strip().upper()

    if can_form_word(word, rack):
        if direction == 'H' and col + len(word) <= 15:
            if is_first_word and (row != 7 or col > 7 or col + len(word) < 7):
                print("\nInvalid first move, word must start from the center as repeated below!")
                return 0
            for i, letter in enumerate(word):
                board[row][col + i] = letter
                rack.remove(letter)
        elif direction == 'V' and row + len(word) <= 15:
            if is_first_word and (col != 7 or row > 7 or row + len(word) < 7):
                print("\nInvalid first move, word must start from the center as repeated below!")
                return 0
            for i, letter in enumerate(word):
                board[row + i][col] = letter
                rack.remove(letter)
        else:
            print("\nInvalid move. Word does not fit on our board.")
            return 0

        score = sum(letter_points[letter] for letter in word)
        print(f"Word played: {word}, Score: {score}")
        return score
    else:
        print("\nYou don't have the letters to play this word. Kindly try again")
        return 0

def draw_tiles(rack):
    while len(rack) < 7 and letter_bag:
        rack.append(letter_bag.pop())

def game_loop():
    player_score = 0
    computer_score = 0

    print("Player's first turn")
    while True:
        player_score += play_word(player_rack, is_first_word=True)
        if player_score > 0:
            break
        print("\nGAME MUST START FROM THE CENTER BOSS!")
    

    draw_tiles(player_rack)

    print("\nComputer's first turn")
    computer_score += play_word(computer_rack, is_computer=True)
    draw_tiles(computer_rack)

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
        print("THE COMPUTER WINS! TRY BETTER NEXT TIME FOR REAL :0 !")

game_loop()
