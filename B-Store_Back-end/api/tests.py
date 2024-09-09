from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from api.models import Book
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken
from django.utils import timezone

class BookAPITest(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(username="testuser", password="testpassword")
        self.book = Book.objects.create(
            title="Test Book",
            author="Test Author",
            description="A test book description.",
            published_date=timezone.now(),
            price=150.00
        )
        # Get JWT token for authentication
        refresh = RefreshToken.for_user(self.user)
        self.token = str(refresh.access_token)
        self.api_authentication()

    def api_authentication(self):
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.token}')

    # Test to retrieve all books
    def test_get_books(self):
        response = self.client.get(reverse("book-list"))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    # Test to retrieve a single book
    def test_get_single_book(self):
        response = self.client.get(reverse("book-detail", kwargs={"pk": self.book.id}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    # Test unauthorized creation of a book
    def test_create_book_unauthorized(self):
        self.client.credentials()  # Remove token
        book_data = {
            "title": "Unauthorized Book",
            "author": "Invalid User",
            "description": "This should not be allowed.",
            "published_date": timezone.now().date(),
            "price": 200.00,
        }
        response = self.client.post(reverse("book-list"), book_data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    # Test authorized creation of a book
    def test_create_book(self):
        book_data = {
            "title": "New Book",
            "author": "Authorized User",
            "description": "This is an authorized post.",
            "published_date": timezone.now().date(),
            "price": 300.00,
        }
        response = self.client.post(reverse("book-list"), book_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    # Test updating a book
    def test_update_book(self):
        update_data = {
            "title": "Updated Book",
            "author": "Updated Author",
            "description": "Updated description.",
            "published_date": timezone.now().date(),
            "price": 350.00,
        }
        response = self.client.put(reverse("book-detail", kwargs={"pk": self.book.id}), update_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    # Test deleting a book
    def test_delete_book(self):
        response = self.client.delete(reverse("book-detail", kwargs={"pk": self.book.id}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


def test_unauthorized_book_update(self):
    self.client.credentials()  # Remove the token to simulate unauthorized user
    response = self.client.put(reverse('book-detail', kwargs={'pk': self.book.id}), {"title": "Updated"})
    self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)


def test_create_book_invalid_data(self):
    invalid_data = {
        "title": "",  # Invalid: Empty title
        "author": "Some Author",
        "description": "No title provided",
        "published_date": timezone.now().date(),
        "price": 150.00,
    }
    response = self.client.post(reverse('book-list'), invalid_data)
    self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class UserAuthenticationTest(APITestCase):

    def setUp(self):
        self.register_url = reverse("register")
        self.login_url = reverse("token_obtain_pair")

    def test_user_registration(self):
        user_data = {
            "username": "newuser",
            "password": "newpassword123",
            "email": "newuser@test.com",
        }
        response = self.client.post(self.register_url, user_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_user_login(self):
        user = User.objects.create_user(username="testuser", password="testpassword")
        response = self.client.post(self.login_url, {"username": "testuser", "password": "testpassword"})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("access", response.data)
