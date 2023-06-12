from .models import User
from rest_framework.generics import RetrieveAPIView
from .serializers import UserSerializer


class UserView(RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class MeUserView(RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_object(self):
        return self.request.user
