from rest_framework import viewsets

from users.models import User
from users.serializers import UserSerializer


# Create your views here.
# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
