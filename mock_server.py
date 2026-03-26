from flask import Flask, request, jsonify

app = Flask(__name__)

books = []
next_id = 1

@app.route('/books', methods=['GET'])
def get_books():
    return jsonify(books), 200

@app.route('/books', methods=['POST'])
def create_book():
    global next_id
    data = request.get_json()
    if not data or not data.get('title') or not data.get('author'):
        return jsonify({"error": "Title and author are required"}), 400
    book = {
        "id": next_id,
        "title": data['title'],
        "author": data['author']
    }
    books.append(book)
    next_id += 1
    return jsonify(book), 201

@app.route('/books/<int:book_id>', methods=['DELETE'])
def delete_book(book_id):
    global books
    book = next((b for b in books if b['id'] == book_id), None)
    if not book:
        return jsonify({"error": "Book not found"}), 404
    books.remove(book)
    return jsonify({"message": "Book deleted"}), 200

if __name__ == '__main__':
    app.run(port=5000)