from flask import Blueprint, jsonify, request
from .models import Flashcard, db

bp = Blueprint('routes', __name__)

@bp.route('/api/flashcards', methods=['GET'])
def get_flashcards():
    flashcards = Flashcard.query.all()
    return jsonify([flashcard.to_dict() for flashcard in flashcards])

@bp.route('/api/flashcards/<int:id>', methods=['GET'])
def get_flashcard(id):
    flashcard = Flashcard.query.get_or_404(id)
    return jsonify(flashcard.to_dict())

@bp.route('/api/flashcards', methods=['POST'])
def create_flashcard():
    data = request.get_json()
    new_flashcard = Flashcard(question=data['question'], answer=data['answer'])
    db.session.add(new_flashcard)
    db.session.commit()
    return jsonify(new_flashcard.to_dict()), 201

@bp.route('/api/flashcards/<int:id>', methods=['PUT'])
def update_flashcard(id):
    # data = request.get_json()
    # flashcard = Flashcard.query.get_or_404(id)
    # flashcard.question = data['question']
    # flashcard.answer = data['answer']
    # db.session.commit()
    # return jsonify(flashcard.to_dict())
    flashcard = Flashcard.query.get_or_404(id)
    db.session.delete(flashcard)
    db.session.commit()
    data = request.get_json()
    new_flashcard = Flashcard(question=data['question'], answer=data['answer'])
    db.session.add(new_flashcard)
    db.session.commit()
    return jsonify(new_flashcard.to_dict()), 201

@bp.route('/api/flashcards/<int:id>', methods=['DELETE'])
def delete_flashcard(id):
    flashcard = Flashcard.query.get_or_404(id)
    db.session.delete(flashcard)
    db.session.commit()
    return '', 204
