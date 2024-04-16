### This is how I mastered Django (all-in-one tutorial)

#### BASIC FIRST STEPS AND CHECKS:

`python --version` - check python version  
`python -m venv .venv` - to create virtual environment   
`source .venv/bin/activate` - to activate virtual environment (`deactivate` to deactivate)  
`python -m pip install Django` - to install Django  
`python -m pip install --upgrade pip` - to upgrade pip  
`python` - to enter python shell (also called REPL), to exit type `exit()`	
`>>> import django` - to check if Django is installed  
`>>> django.get_version()` - to check Django version, also: `print(django.get_version())`  


#### STARTING NEW DJANGO PROJECT:
`django-admin startproject myproject` - to create new project. This will create a folder with project name.  
`cd myproject` - to enter project folder (next command should be run from `myproject` folder)  
`python manage.py runserver` - to run server (verifying that everything is working, we should see Django welcome page at http://127.0.0.1:8000/)  
also `python manage.py runserver 9999` - to specify port number the server will run on.  

#### `urls.py` and `views.py` FILES:
`urls.py` file is used to map URLs to views.  
`urlpatterns` is a list of `path()` functions.  
`path()` function is used to map URLs to views. This function takes 3 arguments: route, view, and kwargs.  
- `route` is a string that contains a URL pattern.
- `view` is a view function that Django will call when the URL pattern is matched.
- `kwargs` is an optional dictionary of keyword arguments.  
   
Adding new URL pattern to the list of urlpatterns:  
```python
...
from django.urls import path
from . import views

urlpatterns = [
	path('admin/', admin.site.urls),
	path('', views.homepage),
	path('about/', views.about),
]
```

`views.py` file is used to define view functions.  
View function is a Python function that takes a web request and returns a web response.  
View function should be imported in `urls.py` file.  
Example of view function:  
```python
from django.http import HttpResponse

def homepage(request):
	return HttpResponse('Hello, World! This is the homepage.')

def about(request):
	return HttpResponse('This is the about page.')
```

After adding new view function to `views.py` and new URL pattern to `urls.py` we can run server and check if new URLs are working. Respective URLs should return the text defined in view functions.  


#### DJANGO TEMPLATES:
To create a new template we need to create a new folder `templates` in the project folder, on the same level as `manage.py` file.  
In the `settings.py` file we need to add the path to the templates folder, which will be used to look for templates:  
```python
TEMPLATES = [
	{
		...
        'DIRS': ['templates'],
		...
	}
]
```

In the `views.py` file we need to import `render` function and use it to render the template:  
```python
from django.shortcuts import render

def homepage(request):
	return render(request, 'home.html')

def about(request):
	return render(request, 'about.html')
```

In the `templates` folder we can create a new HTML files to be used as templates by the views :  
`base.html` - base template that will be extended by other templates.  
`home.html` - template that will extend `base.html`.  
`about.html` - template that will extend `base.html`.  

Example of `base.html` file:
```html
<!DOCTYPE html>
{% load static %}
<html>
<head>
	<meta charset="utf-8">
	<meta name="viewport" content="width=device-width, initial-scale=1">
	<link rel="stylesheet" type="text/css" href="{% static 'css/style.css' %}">

{% block title %}

{% endblock %}

</head>
<body>

{% block content %}

{% endblock %}

</body>
</html>
```  

example of `home.html` file:
```html
{% extends "base.html" %}

{% block title %}
	<title>Home</title>
{% endblock %}

{% block content %}

	<h1>Home</h1>
	<p>Welcome to the home page!</p>
	<p>Check out the <a href="/about">About</a> page.</p>

{% endblock %}
```

#### STATIC FILES:
To serve static files (CSS, JavaScript, images) we need to create a new folder `static` in the project folder, on the same level as `manage.py` file.
Inside the `static` folder we can create subfolders for CSS, JavaScript, images, etc.  

In the `settings.py` file we need to add the path to the static folder, which will be used to look for static files:  
```python
...
import os
...

STATIC_URL = '/static/'

# ..adding the following:
STATICFILES_DIRS = [
	os.path.join(BASE_DIR, 'static'),
]
```  

Now for that to work we add the following to the `Home.html` file:  
```html
<!DOCTYPE html>
{% load static %}
...
	<link rel="stylesheet" type="text/css" href="{% static 'css/style.css' %}">
...
```  
Now the `style.css` is linked to the `home.html` file. All styles defined in `style.css` will be applied to the `home.html` file.  
In the same manner we can link JavaScript files, images, etc.  
in the `base.html` file we can add the following `<script...>` tag to link JavaScript file:  
```html
<head>
	...
	<script src="{% static 'js/script.js' %}" defer></script>
</head>
...
```  
..the `defer` attribute is used to specify that the script is executed when the page has finished parsing / loading.  


#### Chapter 2: Apps & Templates..
(28:00)  


