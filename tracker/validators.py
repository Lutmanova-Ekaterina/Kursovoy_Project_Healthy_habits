import datetime

from django.core.exceptions import ValidationError

from tracker.models import Habit


class Validate_Pleasant:
    """ Привычка, не должна быть связана с другой приятной привычкой"""

    def __init__(self, field):
        self.field = field

    requires_context = True  # Доступ к контексту

    def __call__(self, value, serializer_field):
        hobit_pk = serializer_field.initial_data.get(
            'connection')  # чтобы валидатору передавалось поле сериализатора, с которым он используется, в качестве дополнительного контекста.
        pleasant_connect = Habit.objects.get(pk=hobit_pk)
        if value.get('pleasant'):
            if pleasant_connect.pleasant:
                raise ValidationError('Нельзя связать две приятные привычки!')
            else:
                return True
        return True


class ValidateTimeToComplete:
    """ Привычка не должна расходовать на выполнение больше 2х минут"""

    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        time = value.get('time_to_complete')
        my_max_time = datetime.time(hour=0, minute=2, second=0)
        if time > my_max_time:
            raise ValidationError('привычка не должна расходовать на выполнение больше 2х минут')


class ValidateAward:
    """ исключить одновременный выбор связанной привычки и указания вознаграждения"""

    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        if value.get('award'):
            if value.get('connection'):
                raise ValidationError('Нельзя одновременно выбрать приятную привычку м указание вознаграждения')


class ValidateAwardConnectionNull:
    """нельзя, чтобы связанная привычка и вознаграждение были одновременно пустые"""

    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        if not value.get('pleasant'):
            if (value.get('connection') is None) and (value.get('award') is None):
                raise ValidationError('Нельзя, чтобы связанная привычка и вознаграждение были одновременно пустые')


class ValidatePleasantFalseOrTrue:
    """в связанные привычки могут попадать только привычки с признаком приятной привычки"""

    def __init__(self, field):
        self.field = field

    requires_context = True

    def __call__(self, value, serializer_field):
        hobit_pk = serializer_field.initial_data.get('connection')
        pleasant_connect = Habit.objects.filter(pk=hobit_pk).first()
        if pleasant_connect:
            if not pleasant_connect.pleasant:
                raise ValidationError(
                    'в связанные привычки могут попадать только привычки с признаком приятной привычки')
            else:
                return True


class ValidatePleasantAwardConnection:
    """у приятной привычки не можен быть вознаграждения или связанной привычки"""

    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        if value.get('pleasant'):
            if value.get('connection') is None:
                if value.get('award') is None:
                    return True
                else:
                    raise ValidationError('у приятной привычки не может быть вознагражления или связанной привычки')
            else:
                raise ValidationError('у приятной привычки не может быть вознагражления или связанной привычки')


class ValidateFrequency:
    """периодичность не может быть более 7 дней, то есть привычку нельзя выполнять больше, чем раз в неделю"""

    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        if value.get('frequency'):
            if value.get('frequency') > 7:
                raise ValidationError(
                    'периодичность не может быть более 7 дней, то есть привычку нельзя выполнять больше, чем раз в неделю')
            else:
                return True
        return True
