import random

# Initialize the board (15x15 grid)
board = [[" " for _ in range(15)] for _ in range(15)]
board[7][7] = "  X "

# Example letter points dictionary
letter_points = {
    'A': 1, 'B': 3, 'C': 3, 'D': 2, 'E': 1,
    'F': 4, 'G': 2, 'H': 4, 'I': 1, 'J': 8,
    'K': 5, 'L': 1, 'M': 3, 'N': 1, 'O': 1,
    'P': 3, 'Q': 10, 'R': 1, 'S': 1, 'T': 1,
    'U': 1, 'V': 4, 'W': 4, 'X': 8, 'Y': 4, 'Z': 10
}

letter_bag = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ" * 2)
random.shuffle(letter_bag)
player_rack = [letter_bag.pop() for _ in range(7)]
computer_rack = [letter_bag.pop() for _ in range(7)]

def display_board():
    cell_width = 4
    
    header = "   " + " | ".join(f"{i:<{cell_width}}" for i in range(15)) + " |"
    separator = "  " + "+".join("-" * (cell_width + 2) for _ in range(15)) + "+"

    board_str = header + "\n" + separator + "\n"

    for i in range(15):
        row_header = f"{i:<2} | "
        row_content = " | ".join(f"{board[i][j]:<{cell_width}}" for j in range(15))
        row_str = row_header + row_content + " |"

        board_str += row_str + "\n"
        board_str += separator + "\n"

    print(board_str)


def play_word(rack, is_computer=False):
    display_board()
    if is_computer:
        word = "".join(random.sample(rack, random.randint(1, 3)))
        row, col, direction = random.randint(0, 14), random.randint(0, 14), random.choice(['H', 'V'])
    else:
        print(f"Your rack: {rack}")
        word = input("Enter the word you want to play(from your rack): ").strip().upper()
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
            print("Invalid move. Word does not fit in our board.")
            return 0
        
        score = sum(letter_points[letter] for letter in word)
        print(f"Word played: {word}, Score: {score}")
        return score
    else:
        print("You don't have the letters to play this word. Kindly try again")
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
        print("THE PLAYER WINS!")
    else:
        print("THE COMPUTER WINS!")

game_loop()
