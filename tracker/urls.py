from django.urls import path

from tracker.apps import TrackerConfig
from tracker.views import HabitCreateAPIView, HabitListAPIView, HabitUpdateAPIView, HabitRetrieveAPIView, \
    HabitDestroyAPIView, HabitAllPublicListAPIView

app_name = TrackerConfig.name

urlpatterns = [
    path('habit_create/', HabitCreateAPIView.as_view(), name='habit_create'),
    path('habit_list/', HabitListAPIView.as_view(), name='habit_list'),
    path('habit_update/<int:pk>/', HabitUpdateAPIView.as_view(), name='habit_update'),
    path('habit_retrieve/<int:pk>/', HabitRetrieveAPIView.as_view(), name='habit_retrieve'),
    path('habit_destroy/<int:pk>/', HabitDestroyAPIView.as_view(), name='habit_destroy'),
    path('habit_all_list/', HabitAllPublicListAPIView.as_view(), name='habit_all_list'),
]
