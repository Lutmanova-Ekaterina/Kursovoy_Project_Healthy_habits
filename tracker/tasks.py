# from datetime import timedelta, datetime
# from celery import shared_task
# from tracker.telegram import send_message
#
#
# @shared_task
# def check_time():
#     time = datetime.now().time()
#     time_start = datetime.now() - timedelta(minutes=1)
#     data_habit = Habit.objects.filter(time_gte=time_start)
#     for item in data_habit.filter(time_lte=time):
#         text = f'я буду {item.action} в {item.time} в {item.place}'
#         send_message(text)
