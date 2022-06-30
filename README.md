## 1) Creating a venv
```
python3 -m venv venv
```

## 2) Activating venv
```
source venv/bin/activate

# Windows
venv\Scripts\activate.bat
```

## 3) Installing Django in venv
```
pip install django
```

## 4) Initiating a django project
```
django-admin startproject <project_name> .
```

## 5) Starting the server
```
python3 manage.py runserver
```


### Setting up a page
1) Define a function in views.py
```
def index(request):
    return HttpResponse('Hello, World')
```

2) Link it with urls.py
```
path('', views.index),
```

3) Visit that page

## Adding templates
Adding templates folder to settings.py - DIRS in templates
```
BASE_DIR / 'templates'
```