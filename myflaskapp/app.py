from flask import Flask, render_template

app = Flask(__name__)

# Sample data - could later be replaced with a database
books = [
    {"id": 1, "title": "The Great Gatsby", "author": "F. Scott Fitzgerald", "year": 1925},
    {"id": 2, "title": "1984", "author": "George Orwell", "year": 1949},
    {"id": 3, "title": "To Kill a Mockingbird", "author": "Harper Lee", "year": 1960}
]

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/books')
def show_books():
    return render_template('books.html', books=books)

@app.route('/book/<int:book_id>')
def book_detail(book_id):
    book = next((b for b in books if b["id"] == book_id), None)
    if book:
        return render_template('book_detail.html', book=book)
    return render_template('404.html'), 404

if __name__ == '__main__':
    app.run(debug=True)