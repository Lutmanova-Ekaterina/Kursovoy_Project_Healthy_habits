# import requests
# from django.conf import settings
# from rest_framework.response import Response
#
# from tracker.models import Habit
#
# def send_message(text):
#     habit_data = Habit.objects.last()
#     data_request = {
#         "chat_id": " ",
#         "text": text
#     }
#     responce = requests.get(f"https://api.telegram.org/bot6001611553:AAHMg2Bm6ht__gQ0WLT059o_KqmNvSi-gGw/sendMessage", data_request)
#     return Response(responce.json())
#
#
# import requests
# TOKEN = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjgzNjM5MDg0LCJpYXQiOjE2ODM2MzUzOTUsImp0aSI6IjM4NjAzYWY4ZGFmNjRkMDY5OTU3N2VmMjVhN2NkNDI2IiwidXNlcl9pZCI6MX0.O3WWVev5T9Hx2XfNVJBw-60QBbenxJYqR9gOaeog7wE"
# url = f"https://api.telegram.org/bot6001611553:AAHMg2Bm6ht__gQ0WLT059o_KqmNvSi-gGw/getUpdates"
# print(requests.get(url).json())
