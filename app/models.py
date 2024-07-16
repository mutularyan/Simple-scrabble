from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Member(db.Model):
    __tablename__ = 'Member'

    id = db.Column(db.BigInteger, primary_key=True)
    alias = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)

class game(db.Model): 
    __tablename__ = 'game'
    id = db.Column(db.Integer, primary_key=True)
    member_id = db.Column(db.BigInteger,db.ForeignKey('member.id'),nullable=False,unique=True) 
    board=db.Column(db.Text,nullable=False)

