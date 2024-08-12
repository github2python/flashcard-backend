import os

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY') or 'your_secret_key_here'
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL') or 'mysql://if0_37089114:kyfcn05pT75jq@localhost/if0_37089114_flashcards_db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
