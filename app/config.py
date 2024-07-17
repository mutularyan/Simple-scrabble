#DB Connection
#Environmental variables

from dotenv import load_dotenv

import os

load_dotenv()

conf={
    'dbname':os.getenv('db_name'),
    'user':os.getenv('db_user'),
    'password':os.getenv('db_password'),
    'host':os.getenv('db_host'),
    'port':'6543'
}

class Config:
    SQLALCHEMY_DATABASE_URI="postgresql://postgres.aomlxggghdbyzubwmrhw:zYsG4xfVQXdE4EVg@aws-0-us-east-1.pooler.supabase.com:6543/postgres"
    SQLALCHEMY_TRACK_MODIFICATIONS=False
    JWT_SECRET_KEY=os.getenv('jwt_secret_key')