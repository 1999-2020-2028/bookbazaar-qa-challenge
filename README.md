# BookBazaar QA Challenge — README

## Track
API

## Prereqs
- Python 3.14+
- pip

Install dependencies:
pip install pytest requests flask

## Start Mock Server
Run this command in a terminal:
python mock_server.py

The server will start at http://localhost:5000

## Run Tests
In a second terminal, run:
pytest test_bookbazaar.py -v

## Endpoints / Mapping
- GET /books → returns list of all books
- POST /books → creates a book with { "title": "...", "author": "..." }
- DELETE /books/:id → deletes book by id

## Tests Implemented
- test_create_book_happy_path: POST valid book → assert 201 and correct data returned
- test_create_book_missing_title_returns_400: POST missing title → assert 400 and error message
- test_delete_nonexistent_book_returns_404: DELETE non-existent id → assert 404 and error message

## Design Rationale
I chose the API track using a local Flask mock server for reliability and control. Tests are organized as simple functions following pytest conventions, each targeting one behavior. The mock server resets state on restart, keeping tests isolated. Given more time, I would add a pytest fixture to automatically start and stop the server, removing the need for a manual step.

## Fallback
If the public API is unavailable, start the local mock server with:
python mock_server.py
Then run pytest test_bookbazaar.py -v