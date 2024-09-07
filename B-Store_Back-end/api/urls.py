from django.urls import path
from .views import BookListCreateView, BookDetailView, RegisterView, LoginView
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path('', BookListCreateView.as_view(), name='book-list-create'),
    path('book/<int:id>/', BookDetailView.as_view(), name='book-detail'),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
