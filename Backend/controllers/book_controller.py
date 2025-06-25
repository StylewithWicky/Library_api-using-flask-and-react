from flask import Blueprint,jsonify,request
from service.openlibrary_service import fetch_books

book_bp= Blueprint('books',__name__)

@book_bp.route('/api/books', methods=['GET'])
def get_books():
    query=request.args.get('q')
    if not query:
        return{f'error':'Query string  required'},400
    books=fetch_books(query)
    return jsonify(books)
