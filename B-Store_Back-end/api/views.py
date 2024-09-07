from rest_framework import status
from rest_framework.response import Response
# from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from blog.models import Book
from .serializers import BookSerializer

class BookListCreateView(ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def post(self, request, *args, **kwargs):
        # only authenticated users
        if not request.user.is_authenticated:
            return Response({'detail':'Authentication required'}, status=status.HTTP_401_UNAUTHORIZED)
        return super().post(request, *args, **kwargs )

class BookDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    lookup_field = 'id'

    def put(self,request, *args, **kwargs):
        if not request.user.is_authenticated:
            return Response({'detail':'Authentication required'}, status=status.HTTP_401_UNAUTHORIZED)
        return super().put(request, *args, **kwargs)
    
    def delete(self,request,*args, **kwargs):
        if not request.user.is_authenticated:
            return Response({'detail':'Authentication required'}, status=status.HTTP_401_UNAUTHORIZED)
        return super().delete(request, *args, **kwargs)
    


from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import UserSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

class RegisterView(APIView):
    def post(self,request):
        serializer = UserSerializer(data = request.data)
        if serializer.is_valid():
            user = serializer.save()
            refresh = RefreshToken.for_user(user)
            return Response({
                'refresh': str(refresh),
                'access' : str(refresh.access_token),
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginView(TokenObtainPairView):
    pass   