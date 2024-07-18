from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required,get_jwt_identity
from models import db, Game
from game_engine import create_board, letter_bag_rack
import json
from util import to_int

game_blueprint=Blueprint('game',__name__)


@game_blueprint.route("/game/board", methods=["GET"])
@jwt_required()
def get_board() -> jsonify:
    current_user = get_jwt_identity()
    print(current_user)
    game = Game.query.filter_by(member_id=current_user['id']).first()
    print(game)
    if not game:
       return jsonify({'message': 'Game does not exist'}), 404
    board = json.loads(game.board)
    return jsonify({'message': f"Hi, {current_user['user_name']} this is your board", 'board':board})

"""
@game_blueprint.route("/game/rack", methods=["GET"])
@jwt_required()
def get_rack():
    current_user = get_jwt_identity()
    print(current_user)
    game = Game.query.filter_by(member_id=current_user['id']).first()
    if not game:
       return jsonify({'message': 'Game does not exist'}), 404

    rack = []
    for _ in range(7):
        tile = letter_bag.pop()
        rack.append(tile)

    game.rack = json.dumps(rack)
    db.session.commit()
    return jsonify({'message': f"{current_user['user_name']} rack", 'rack': rack})
"""
