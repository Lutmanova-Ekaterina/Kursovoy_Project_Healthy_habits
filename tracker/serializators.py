from rest_framework import serializers

from tracker.models import Habit
# from tracker.validators import Validate_Pleasant, ValidateTimeToComplete, ValidateAward, ValidateAwardConnectionNull, \
#     ValidatePleasantFalseOrTrue, ValidatePleasantAwardConnection, ValidateFrequency


class HabitSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Habit
        fields = '__all__'
        # validators = [
        #     Validate_Pleasant(field=('pleasant', 'connection')),
        #     ValidateTimeToComplete(field='time_to_complete'),
        #     ValidateAward(field=('award', 'connection')),
        #     ValidateAwardConnectionNull(field=('pleasant', 'connection', 'award')),
        #     ValidatePleasantFalseOrTrue(field='pleasant'),
        #     ValidatePleasantAwardConnection(field=('pleasant', 'connection', 'award')),
        #     ValidateFrequency(field='frequency')
        # ]
