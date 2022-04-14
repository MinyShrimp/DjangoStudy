
# Django REST Framework 학습

## URL
https://www.inflearn.com/course/%EC%9E%A5%EA%B3%A0-drf/dashboard

## install
```
python -m venv venv
source venv/bin/activate

pip install django djangorestframework
django-admin startproject mysite .
python manage.py startapp blog

python manage.py makemigrations
python manage.py migrate
python manage.py runserver

pip freeze > requirements.txt
pip install -r requirements.txt
```