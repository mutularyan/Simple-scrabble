import random

board = [[" " for _ in range(15)] for _ in range(15)]
board[7][7] = "  X "
board[0][0] = " TW "
board[0][3] = " DL "
board[0][7] = " TW "
board[0][11] = " DL "
board[0][14] = " TW " 
board[1][1] = " DW "
board[1][5] = " TL "
board[1][9] = " TL "
board[1][13] = " DW "
board[2][2] = " DW "
board[2][6] = " DL"
board[2][8] = " DL " 
board[2][12] = " DW "
board[3][0] = " DL "
board[3][3] = " DW "
board[3][7] = " DL "
board[3][11] = " DW "
board[3][14] = " DL "
board[4][4] = " DW " 
board[4][10] = " DW "
board[5][1] = " TL "
board[5][5] = " TL "
board[5][9] = " TL "
board[5][13] = " TL "
board[6][2] = " DL"
board[6][6] = " DL " 
board[6][8] = " DL "
board[6][12] = " DL "
board[7][0] = " TW "
board[7][3] = " DL "
board[7][11] = " DL "
board[7][14] = " TW "
board[8][2] = " DL " 
board[8][6] = " DL "
board[8][8] = " DL "
board[8][12] = " DL "
board[9][1] = " TL "
board[9][5] = " TL "
board[9][9] = " TL"
board[9][13] = " TL " 
board[10][4] = " DW "
board[10][10] = " DW "
board[11][0] = " DL "
board[11][3] = " DW "
board[11][7] = " DL "
board[11][11] = " DW "
board[11][14] = " DL " 
board[12][2] = " DW "
board[12][6] = " DL "
board[12][8] = " DL "
board[12][12] = " DW "
board[13][1] = " DW "
board[13][5] = " TL"
board[13][9] = " TL " 
board[13][13] = " DW "
board[14][0] = " TW "
board[14][3] = " DL"
board[14][7] = " TW " 
board[14][11] = " DL "
board[14][14] = " TW "

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
