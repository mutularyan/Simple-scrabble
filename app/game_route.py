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
    game = Game.query.filter_by(member_id=current_user['member_id']).first()
    print(game)
    if not game:
       return jsonify({'message': 'Game does not exist'}), 404
    board = json.loads(game.board)
    return jsonify({'message': f"Hi, {current_user['user_name']} this is your board", 'board':board})


@game_blueprint.route("/game/rack", methods=["PUT"])
@jwt_required()
def get_rack():
    current_user = get_jwt_identity()
    print(current_user)
    game = Game.query.filter_by(member_id=current_user['member_id']).first()
    if not game:
       return jsonify({'message': 'Game does not exist'}), 404

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

    game.rack = json.dumps(player_rack)
    db.session.commit()
    return jsonify({'message': f"{current_user['user_name']} rack", 'rack':player_rack})


@game_blueprint.route("/game/make_move", methods=["PUT"])
@jwt_required()
def human_move():
    current_user = get_jwt_identity()
    game = Game.query.filter_by(member_id=current_user['member_id']).first()

    if not game:
        return jsonify({'message': 'Game does not exist'}), 404

    request_data = request.get_json()
    if not request_data or 'board' not in request_data or 'word' not in request_data or 'position' not in request_data or 'direction' not in request_data:
        return jsonify({'message': 'Invalid request data'}), 400

    direction = request_data['direction']
    position = request_data['position']
    x = to_int(position.get('x'))
    y = to_int(position.get('y'))
    word = request_data['word']

    if x is None or y is None or not word or direction not in ["right", "down"]:
        return jsonify({'message': "Invalid Input"}), 400
    


    board = json.loads(game.board)
    new_board = Board()
    new_board.board = board

    return jsonify({'message': f"Hi {current_user['username']} this is your board", 'board': new_board.board}), 200
