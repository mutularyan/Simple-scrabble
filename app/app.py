from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import Config
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity
from models import db, Member, Game  # Ensures correct import order
from game_engine import create_board
import json

# Initialize Flask extensions
bcrypt = Bcrypt()
migrate = Migrate()
jwt = JWTManager()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)
    bcrypt.init_app(app)
    jwt.init_app(app)
    migrate.init_app(app, db)   
    return app

app = create_app()

with app.app_context():
    db.create_all()

@app.route('/')
def sam():
    return 'sam'

@app.route("/signup", methods=["POST"])
def signup():
    data = request.get_json()
    user_name = data.get('user_name')
    email = data.get('email')
    password = data.get('password')

    # Validation
    if not email or not password or not user_name:
        return jsonify({'message': "Required field missing"}), 400

    if len(email) < 4:
        return jsonify({'message': "Email too short"}), 400

    if len(user_name) < 4:
        return jsonify({'message': "Name too short"}), 400

    if len(password) < 4:
        return jsonify({'message': "Password too short"}), 400

    existing_member = Member.query.filter_by(email=email).first()

    if existing_member:
        return jsonify({'message': f"Email already in use {email}"}), 400

    hashed_password = bcrypt.generate_password_hash(password).decode('utf8')  # decoded to store the password in the database

    member = Member(user_name=user_name, email=email, password=hashed_password)
    db.session.add(member)
    db.session.commit()
    return jsonify({"message": "Account created successfully"}), 201

@app.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')

    # Validation
    if not email or not password:
        return jsonify({'message': "Required field missing"}), 400

    user = Member.query.filter_by(email=email).first()

    print(user.game)

    if not user:
        return jsonify({'message': "User not found"}), 400

    pass_ok = bcrypt.check_password_hash(user.password.encode('utf-8'),password)
    
    # ACCESS TOKEN
    access_token = create_access_token(identity=user.email)
    if not pass_ok:
        return jsonify({'message': "Invalid password"}), 401
    return jsonify({'user': {'user_name': user.user_name, 'email': user.email}, 'token': access_token})

    if not user.game:
        member_id = user.id
        board = json.dumps(create_board())
        print(board)
        game = Game(member_id=member_id, board=board)
        db.session.add(game)
        db.session.commit()

@app.route("/game/board", methods=["GET"])
@jwt_required()
def get_board():
    current_user = get_jwt_identity()
    print(current_user)
    return jsonify({'message': f"Hi this is your board"})


#get board
#new game
#make move

if __name__ == '__main__':
    app.run(debug=True, port=9000)