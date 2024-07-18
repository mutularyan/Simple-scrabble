from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Member(db.Model):
    __tablename__ = 'member'

    id = db.Column(db.BigInteger, primary_key=True)
    user_name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    game=db.relationship('Game',backref='member',uselist=False,cascade='all, delete-orphan')

    def info(self):
        return{'id':self.id, 'user_name':self.user_name, 'email':self.email}

class Game(db.Model): 
    __tablename__ = 'game'
    id = db.Column(db.Integer, primary_key=True)
    member_id = db.Column(db.BigInteger,db.ForeignKey('member.id', ondelete = 'CASCADE'), nullable=False,unique=True) 
    board=db.Column(db.Text,nullable=False)
    player_rack = db.Column(db.Text, nullable=False) 
    tile_bag = db.Column(db.Text, nullable=False)
    player_score = db.Column(db.Integer, nullable=False, default=0)
    computer_rack = db.Column(db.Text, nullable=False)
    computer_score = db.Column(db.Integer, nullable=False, default=0)


    def game_state(self):
        return {
            'board': self.board,
            'player_rack': self.player_rack,
            'tile_bag': self.tile_bag,
            'player_score': self.player_score,
            'computer_rack': self.computer_rack,
            'computer_score': self.computer_score
        }
