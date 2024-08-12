import os

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY') or 'your_secret_key_here'
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL') or 'mysql://root:55sS%401025@localhost/flashcards_db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
