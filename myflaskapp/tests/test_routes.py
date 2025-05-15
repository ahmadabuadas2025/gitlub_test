import unittest

from app import app, books

class TestFlaskApp(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_home_page_status_code(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Welcome to the Book Library', response.data)

    def test_books_route(self):
        response = self.app.get('/books')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'The Great Gatsby', response.data)

    def test_book_detail_exists(self):
        response = self.app.get('/book/1')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'F. Scott Fitzgerald', response.data)

    def test_book_detail_not_found(self):
        response = self.app.get('/book/999')
        self.assertEqual(response.status_code, 404)

    def test_book_count_in_index(self):
        response = self.app.get('/')
        self.assertIn(f'We currently have {len(books)} books'.encode(), response.data)

if __name__ == '__main__':
    unittest.main()