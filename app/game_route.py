from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required,get_jwt_identity
from models import db, Game
from game_engine import create_board, letter_bag_rack
import json
from util import to_int
import random

game_blueprint=Blueprint('game',__name__)

@game_blueprint.route("/game/board", methods=["GET"])
@jwt_required()
def get_board():
    current_user = get_jwt_identity()
    print(current_user)

    user_id = current_user['member_id']  
    game = Game.query.filter_by(member_id=user_id).first()
    print(game)
    
    if not game:
        return jsonify({'message': 'Game not found'}), 400

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
    player_rack = []
    for _ in range(7):
        tile = letter_bag.pop()
        player_rack.append(tile)

    game.player_rack = json.dumps(player_rack)
    db.session.commit()
    return jsonify(
        {
        'message': f"Hi {current_user['user_name']} this is your board and your rack",
        'board': json.loads(game.board),
        'player_rack': player_rack
        }
    ), 400

@game_blueprint.route("/game/make_move", methods=["PUT"])
@jwt_required()
def make_move():
    body = request.get_json()
    word = body.get("word")
    row = body.get("row")
    col = body.get("col")
    direction = body.get("direction").upper()

    if not word or row is None or col is None or not direction:
        return jsonify({"message": "Required fields missing"}), 400

    current_user = get_jwt_identity()
    game = Game.query.filter_by(member_id=current_user['user_name']).first()
    if not game:
        return jsonify({'message': "Game not found"}), 400

    board = json.loads(game.board)
    player_rack = json.loads(game.player_rack)

    if not can_form_word(word, player_rack):
        return jsonify({"message": "Invalid move: word cannot be formed from your rack"}), 400

    valid_move = True
    if direction == 'H':
        if col + len(word) > 15:
            valid_move = False
        for i, letter in enumerate(word):
            if board[row][col + i] not in [" ", letter]:
                valid_move = False
                break
    elif direction == 'V':
        if row + len(word) > 15:
            valid_move = False
        for i, letter in enumerate(word):
            if board[row + i][col] not in [" ", letter]:
                valid_move = False
                break
    else:
        return jsonify({"message": "Invalid direction"}), 400

    if not valid_move:
        return jsonify({"message": "Invalid move: word cannot be placed on the board"}), 400

    if direction == 'H':
        for i, letter in enumerate(word):
            board[row][col + i] = letter
            player_rack.remove(letter)
    elif direction == 'V':
        for i, letter in enumerate(word):
            board[row + i][col] = letter
            player_rack.remove(letter)

    
    letter_bag = json.loads(game.tile_bag)
    draw_tiles(player_rack, letter_bag)
    
    game.board = json.dumps(board)
    game.player_rack = json.dumps(player_rack)
    game.tile_bag = json.dumps(letter_bag)
    db.session.commit()

    return jsonify({'message': f"Hi {current_user['username']} this is your board", 'board': new_board.board, 'score': game.player_score}), 200

@game_blueprint.route("/game/new-game", methods=["POST"])
@jwt_required()
def new_game():
    current_user = get_jwt_identity()
    game = Game.query.filter_by(member_id=current_user['user_name']).first()
    if game:
        return jsonify({'message': "Game already exists"}), 400
   
    board = create_board()

    letter_bag = []
    for letter, count in letter_no.items():
        letter_bag.extend([letter] * count)
    random.shuffle(letter_bag)
    player_rack = [letter_bag.pop() for _ in range(7)]
   
    board_json = json.dumps(board)
    tile_bag_json = json.dumps(letter_bag)
    player_rack_json = json.dumps(player_rack)
    
    game = Game(
        member_id=current_user['id'],
        board=board_json,
        tile_bag=tile_bag_json,
        player_rack=player_rack_json
    )

    db.session.add(game)
    db.session.commit()

    return jsonify({'message': "New game created", 'board': board, 'player_rack': player_rack})

