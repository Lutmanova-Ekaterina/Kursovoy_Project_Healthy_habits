from django.urls import path

from users.apps import UsersConfig
from users.views import UserRetrieveAPIView, UserUpdateAPIView, RegisterAPIView

app_name = UsersConfig.name

urlpatterns = [
    path('register/', RegisterAPIView.as_view(), name='register'),
    path('<int:pk>/', UserRetrieveAPIView.as_view(), name='retrieve'),
    path('update/<int:pk>/', UserUpdateAPIView.as_view(), name='update'),
]
