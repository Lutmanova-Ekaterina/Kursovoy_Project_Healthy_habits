from rest_framework.generics import CreateAPIView, UpdateAPIView, ListAPIView, RetrieveAPIView, DestroyAPIView
from rest_framework.permissions import IsAuthenticated
from tracker.permissions import UserPermissions
from tracker.models import Habit
from tracker.serializators import HabitSerializer


class HabitCreateAPIView(CreateAPIView):
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
    # permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        """переопределяем, чтобы сохранился"""
        serializer.save(user=self.request.user)
        # check_time.delay()


class HabitUpdateAPIView(UpdateAPIView):
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
    # permission_classes = [IsAuthenticated, UserPermissions] #только для пользователя


class HabitListAPIView(ListAPIView):
    queryset = Habit.objects.all()  # queryset обязательный - Это набор запросов, в отношении которого должна обеспечиваться уникальность.
    serializer_class = HabitSerializer

    # permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Habit.objects.filter(user=self.request.user)  # только свои привычки


class HabitRetrieveAPIView(RetrieveAPIView):
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
    # permission_classes = [IsAuthenticated, UserPermissions] #только для пользователя


class HabitDestroyAPIView(DestroyAPIView):
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
    # permission_classes = [IsAuthenticated, UserPermissions] #только для пользователя


class HabitAllPublicListAPIView(ListAPIView):
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer

    # permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Habit.objects.filter(status_public=Habit.STATUSE_PUBLIC)  # спмсок убличных привычек
