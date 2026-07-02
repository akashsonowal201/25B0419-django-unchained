from rest_framework import generics, permissions
from .models import Bounty
from .serializers import BountySerializer
from django.contrib.auth.models import User
from rest_framework import generics, permissions
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .serializers import RegisterSerializer
from rest_framework.response import Response
from django.core.cache import cache


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [permissions.AllowAny]


class BountyListCreateView(generics.ListCreateAPIView):

    serializer_class = BountySerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Bounty.objects.filter(owner=self.request.user)

    def list(self, request, *args, **kwargs):
        cache_key = f"bounties_{request.user.id}"

        cached_data = cache.get(cache_key)

        if cached_data:
            return Response(cached_data)

        response = super().list(request, *args, **kwargs)

        cache.set(cache_key, response.data, timeout=60)

        return response

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

       
        cache.delete(f"bounties_{self.request.user.id}")


class BountyDetailView(generics.RetrieveUpdateDestroyAPIView):

    serializer_class = BountySerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Bounty.objects.filter(owner=self.request.user)

    def perform_update(self, serializer):
      serializer.save()
      cache.delete(f"bounties_{self.request.user.id}")


def perform_destroy(self, instance):

    instance.delete()

    cache.delete(f"bounties_{self.request.user.id}")
