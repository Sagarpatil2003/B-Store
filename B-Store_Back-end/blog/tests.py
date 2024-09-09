from django.test import TestCase
from .models import Book
from django.utils import timezone


class BookModelTest(TestCase):

    def setUp(self):
        self.book = Book.objects.create(
            title="Sample Book",
            author="John Doe",
            description="A sample book description.",
            published_date=timezone.now(),
            price= 100.00
        )
        
    def book_creation_test(self):
        self.assertEqual(self.book.title,"Sample Book")
        self.assertEqual(self.book.author,"John Doe")
        self.assertTrue(self.book.created_at)
    
    def test_book_string_representation(self):
        self.assertEqual(str(self.book),self.book.title)
    
    def  test_book_clean(self):
        with self.assertRaisesMessage(ValueError, "The title field cannot be empty."):
            self.book.title=''
            self.book.full_clean()


