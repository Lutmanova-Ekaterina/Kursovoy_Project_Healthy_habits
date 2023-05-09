FROM python:3.11

WORKDIR / code

RUN pip install django
RUN pip install psycopg2
RUN pip install django-cors-headers
RUN pip install djangorestframework
RUN pip install Pillow
RUN pip install celery
RUN pip install django-celery-beat
RUN pip install djangorestframework-simplejwt
RUN pip install drf-yasg
RUN pip install redis
RUN pip install requests

COPY . .

CMD python manage.py runserver 0.0.0.0:8000
