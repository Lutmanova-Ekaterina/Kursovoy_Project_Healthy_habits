from rest_framework.test import APITestCase
from rest_framework import status

from tracker.models import Habit
from users.models import User


class HabitTestCase(APITestCase):
    def setUp(self) -> None:
        test_email = 'test@case.ru'
        test_password = 'test123'

        self.user = User(
            email=test_email,
            first_name='First',
            last_name='Last',
            telegram_id='0987654321'
        )
        self.user.set_password(test_password)
        self.user.save()

        response = self.client.post(
            '/api/token/',
            {
                'email': test_email,
                'password': test_password
            }
        )
        self.access_token = response.json().get('access')
        self.client.credentials(HTTP_AUTHORIZATION=f'Brearer {self.access_token}')

    def test_habit_create(self):
        self.test_place = "test place"
        self.test_time = "11:11"
        self.test_action = "test action"
        self.test_pleasant = False
        self.test_connection = None
        self.test_frequency = 1
        self.test_award = "test award"
        self.test_time_complete = "00:60"
        self.test_status_public = True

        response = self.client.post(
            '/habit_create/',
            {
                "place": self.test_place,
                "time": self.test_time,
                "action": self.test_action,
                "pleasant": self.test_pleasant,
                "connection": self.test_connection,
                "frequency": self.test_frequency,
                "award": self.test_award,
                "time_complete": self.test_time_complete,
                "status_public": self.test_status_public
            }
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        test_habit = Habit.objects.first()
        self.test_pk = test_habit.pk

    def test_habit_retrieve(self):
        self.test_habit_create()
        response = self.client.get(
            f'/habit_retrieve/{self.test_pk}/'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertEqual(
            response.json(),
            {
                "place": self.test_place,
                "time": self.test_time,
                "action": self.test_action,
                "pleasant": self.test_pleasant,
                "connection": self.test_connection,
                "frequency": self.test_frequency,
                "award": self.test_award,
                "time_complete": self.test_time_complete,
                "status_public": self.test_status_public
            }
        )

    def test_habit_list(self):
        self.test_habit_create()
        response = self.client.get(
            '/habit_list/'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertEqual(
            response.json(),
            [{
                "place": self.test_place,
                "time": self.test_time,
                "action": self.test_action,
                "pleasant": self.test_pleasant,
                "connection": self.test_connection,
                "frequency": self.test_frequency,
                "award": self.test_award,
                "time_complete": self.test_time_complete,
                "status_public": self.test_status_public
            }]
        )

    def test_habit_update(self):
        self.test_habit_create()
        self.test_update_place = 'update' + self.test_place
        response = self.client.patch(
            f'/habit_update/{self.test_pk}/',
            {
                "place": self.test_update_place,
            }
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertEqual(
            response.json(),
            [{
                "place": self.test_update_place,
                "time": self.test_time,
                "action": self.test_action,
                "pleasant": self.test_pleasant,
                "connection": self.test_connection,
                "frequency": self.test_frequency,
                "award": self.test_award,
                "time_complete": self.test_time_complete,
                "status_public": self.test_status_public
            }]
        )

    def test_habit_destroy(self):
        self.test_habit_create()
        response = self.client.delete(
            f'habit_destroy/{self.test_pk}/'
        )
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
