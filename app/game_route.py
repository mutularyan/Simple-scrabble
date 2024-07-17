from flask import Blueprint,jsonify,request
from flask_jwt_extended import jwt_required,get_jwt_identity
from models import db, Game
from game_engine import create_board


game_blueprint=Blueprint('game',__name__)

@game_blueprint.route("/game/board", methods=["GET"])
@jwt_required()
def get_board():
    current_user = get_jwt_identity()
    print(current_user)
    game = Game.query.filter_by(member_id=current_user['id']).first()
    print(game)
    if not game:
       return jsonify({'message': 'Game does not exist'}), 404
    board = json.dumps(game.board)
    return jsonify({'message': f"Hi, {current_user['user_name']} this is your board", 'board':board})

@
