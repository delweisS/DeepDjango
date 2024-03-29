from django.contrib.auth import get_user_model
from rest_framework import viewsets

from posts.models import Post
from .permissions import IsAuthorOrReadOnly
from .serializers import PostSerializer, UserSerializer


class PostAPIView(viewsets.ModelViewSet):
	permission_classes = (IsAuthorOrReadOnly,)
	queryset = Post.objects.all()
	serializer_class = PostSerializer


class UserAPIView(viewsets.ModelViewSet):
	queryset = get_user_model().objects.all()
	serializer_class = UserSerializer
