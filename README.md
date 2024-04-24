## This is how I mastered Django (all-in-one tutorial)

### BASIC FIRST STEPS AND CHECKS:

`python --version` - check python version  
`python -m venv .venv` - to create virtual environment   
`source .venv/bin/activate` - to activate virtual environment (`deactivate` to deactivate)  
`python -m pip install Django` - to install Django  
`python -m pip install --upgrade pip` - to upgrade pip  
`python` - to enter python shell (also called REPL),  
`>>> exit()` - to exit type  
`>>> import django` - to check if Django is installed  
`>>> django.get_version()` - to check Django version, also: `print(django.get_version())`  

`pip install Pillow` - to install Pillow package (explained later in ADDING IMAGES).  


### STARTING NEW DJANGO PROJECT:
`django-admin startproject myproject` - to create new project. This will create a folder with project name.  
`cd myproject` - to enter project folder (next command should be run from `myproject` folder)  
`python manage.py runserver` - to run server (verifying that everything is working, we should see Django welcome page at http://127.0.0.1:8000/)  
also `python manage.py runserver 9999` - to specify port number the server will run on (default is 8000).  

## ABOUT `urls.py` and `views.py` FILES:
`urls.py` file is used to map URLs to views.  
`urlpatterns` is a list of `path()` functions.  
`path()` function is used to map URLs to views. This function takes 3 arguments: route, view, and kwargs.  
- `route` is a string that contains a URL pattern.
- `view` is a view function that Django will call when the URL pattern is matched.
- `kwargs` is an optional dictionary of keyword arguments.  
   
Adding new URL pattern to the list of `urlpatterns`:  
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

Example of view functions `homepage` and `about` in `views.py` file:  
```python
from django.http import HttpResponse

def homepage(request):
	return HttpResponse('Hello, World! This is the homepage.')

def about(request):
	return HttpResponse('This is the about page.')
```  
   

After adding new view function to `views.py` and new URL pattern to `urls.py` we can run server and check if new URLs are working. Respective URLs should return the text defined in view functions.  
   

## DJANGO TEMPLATES:
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

<details>
<summary>Example of `base.html` or `layout.html` file:</summary>

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
</details>  


<details>
<summary>Example of `home.html` file:</summary>

```html
{% extends "layout.html" %}
{% block title %}
	<title>Home</title>
{% endblock %}
{% block content %}
	<h1>Home</h1>
	<p>Welcome to the home page!</p>
	<p>Check out the <a href="/about">About</a> page.</p>
{% endblock %}
```  
</details>


## STATIC FILES AND TEMPLATES:
To serve static files (CSS, JavaScript, images) we need to create a new folder `static` in the project folder, on the same level as `manage.py` file.
Inside the `static` folder we can create subfolders for CSS, JavaScript, images, etc.  

In the `settings.py` file we need to add the path to the static folder, which will be used by django to look for static files:  
<details>
<summary>Adding `STATICFILES_DIRS` to `settings.py`. Click to expand..</summary>

```python
...
import os
...
...
STATIC_URL = '/static/'
# ..adding the following:
STATICFILES_DIRS = [
	os.path.join(BASE_DIR, 'static'),
]
```  
</details>

Now for that to work we add the following to the `Home.html` file:  
<details>
<summary>Adding `link` tag to Home.html</summary>

```html
<!DOCTYPE html>
{% load static %}
...
	<link rel="stylesheet" type="text/css" href="{% static 'css/style.css' %}">
...
```  
</details>

Now the `style.css` is linked to the `home.html` file. All styles defined in `style.css` will be applied to the `home.html` file only!  

In the same manner we can link JavaScript files, images, etc.  

For the stylesheets as well as scripts it is a common practice to add the reference to the `base.html` or `layout.html` file, so that they are applied to all templates that extend the `base.html` file.    

in the `base.html` file we can add the `<script...>` and `<link..>` tags to link static files to the template.:  
<details>
<summary>Example of `layout.html` file with reference to static files. Click to expand..</summary>

```html
<!DOCTYPE html>
{% load static %}
<html lang="en">
<head>
	<meta charset="UTF-8">
	<meta name="viewport" content="width=device-width, initial-scale=1.0">
	<title>
		{% block title %}
			Django App
		{% endblock %}
	</title>
	<link rel="stylesheet" type="text/css" href="{% static 'css/style.css' %}">
	<script src="{% static 'js/script.js' %}" defer></script>
</head>
<body>
	<nav>
		<a href="/">Home</a> |
		<a href="/about">About</a> |
		<a href="/posts">Posts</a> |
	</nav>
	<main>
		{% block content %}
		{% endblock %}
	</main>
	
</body>
</html>
```  
</details>

..the `defer` attribute in `<script..>` tag is used to specify that the script is executed when the page has finished parsing / loading.  


## DJANGO APPS:  

`python manage.py startapp posts` - to create a new app (posts here is a name for a new django app).  

The directory with the `app_name` will be created in the root of project folder (`myproject` in the case of this tutorial).  

This `app` / `directory name` need to be added to the `INSTALLED_APPS` list in the `settings.py` file of the `myproject` folder:  

```python
INSTALLED_APPS = [
	...
	'posts',
]
```

In the `posts` app folder we create a new directory `templates` and inside that directory we create another directory `posts` - this is colled a `namespace` for the templates of the `posts` app.  
Inside the `posts` directory we create a new HTML file `home.html` - this is a template for the `home` view of the `posts` app.  

*!!! To be able to use the **`html` default syntax** to create html template we can go to `settings` and search for `emmet` and add a new item to `Emmet: Include Languages`:
`django-html` as Item and `html` as Value.*  

This will allow us to use `html` syntax in the `html` files by typing `!` and pressing `Tab`.  

## MODELS AND DATABASES:

Models in Django are used to define the structure of the database. The models contain fields and methods / behaviors of the data stored in the database `db.sqlite3` by default in the root of the project folder.  

Generaly each model maps to a single database table.  

The `models.py` file in the app folder is used to define models. Each model is represented by a class that inherits from `django.db.models.Model`.  
Each attribute of the model class represents a field in the database table.  
More about models in [Django docs, models](https://docs.djangoproject.com/en/5.0/ref/models/).

For example, a model `Post` for a blog post can be defined as follows:  

```python
from django.db import models

class Post(models.Model):
	title = models.CharField(max_length=100)
	body = models.TextField()
	slug = models.SlugField()
	date = models.DateTimeField(auto_now_add=True)
```

More about `CharField`, `TextField` etc in the docs for [field types](https://docs.djangoproject.com/en/5.0/ref/models/fields/).  

These models become database tables when we run the `migrate` command.   

When we use the command `python manage.py runserver` there is an error that says that there are unapplied migrations.  
`python manage.py migrate` - to apply default migrations used by the Django from builtin models. After this the error will dissapear.  

`python manage.py makemigrations` - to create new migrations based on the changes made to the cusom models, created by the user.  
After this command we can see the new migration file in the `migrations` folder of the app (`posts/migrations/0001_initial.py`).  

`python manage.py migrate` - to apply the new migrations to the database.  

### ORM (Object-Relational Mapping):
Django uses ORM to interact with the database.  
ORM is a programming technique that maps objects to database tables.  

We can interact with the database using the Django shell:  

`python manage.py shell` - to enter the Django shell.  
`>>> exit()` - to exit the Django shell.  
`>>> from posts.models import Post` - to import the `Post` model.  
`>>> p = Post()` - to create a new instance of the `Post` model.   
`>>> p.title = 'My first post'` - to set the title of the post.  
`>>> p.save()` - to save the post to the database.  
`>>> Post.objects.all()` - to get all posts from the database.  
The last command will return a list of all posts in the database as a number of `Post` objects.  
To change that and return, for example a list of titles of the posts we can add additional method to the `Post` model:  

```python
class Post(models.Model):
	title = models.CharField(max_length=100)
	body = models.TextField()
	slug = models.SlugField()
	date = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.title
```
The `__str__` method is a special method that returns a string representation of the object.  

After adding the `__str__` method to the `Post` model we can run the `Post.objects.all()` command in the Django shell and it will return a list of titles of the posts.  

## ADMIN PANEL: 

by visiting the `http://localhost:8000/admin/` we can see the admin panel.  

Admin panel is a built-in Django feature that allows us to manage the database using a web interface.  
It is quick and convenient way to manage the website content / database.  

The admin panel is automatically created when we create a new project. It requires a `superuser` to log in, which can be created using the following command:  

`python manage.py createsuperuser` - to create a new superuser.  

This will prompt to enter the username, email(optional) and password(at least 8 characters and not too common) for the new superuser.  
After creating the superuser we can log in to the admin panel using the credentials we just created.  

The admin panel is empty by default (contains only `users` and `groups`) and it can be customized by creating a new model in `admin.py` file in the app folder `myproject/posts/admin.py`:  

```python
from django.contrib import admin
from .models import Post

admin.site.register(Post)
```

This will add the `Post` model to the admin panel, so we can manage the posts from the admin panel.  

To add / render the data from the database on the website we update the `views.py` file in the app folder `myproject/posts/views.py`:  

```python
from django.shortcuts import render
from .models import Post

# Create your views here.
def posts_list(request):
	posts = Post.objects.all() # this will return all the posts
	return render(request, 'posts/posts_list.html', {'posts': posts}) # this will render the request to the template posts_list.html
```
..`{'posts': posts}` is a dictionary that contains the key `posts` and the value `posts` which is a list of all posts.  

We then change the `posts_list.html` file in the `myproject/posts/templates/posts` folder to render the posts on the website:    

```html
{% extends "layout.html" %}
{% block title %}
	<title>Posts</title>
{% endblock %}
{% block content %}
	<h1>posts</h1>
	{% for post in posts %}
		<h2>{{ post.title }}</h2>
		<p>{{ post.date }}</p>
		<p>{{ post.body }}</p>
	{% endfor %}
{% endblock %}
```

..`{% for post in posts %}` is a loop that iterates over the `posts` list and renders the title, body and date of each post.  


## PAGES, URLs, SLUGS AND DYNAMIC URLs:

Using the `urls.py` file in the app folder (`myproject/posts/urls.py`) using `.name` attribute we can create a name for the URL pattern:  

```python
from django.urls import path
from . import views

urlpatterns = [
	path('', views.posts_list, name='posts'),
]
```

This named link will allow us to use the name of the URL pattern in the templates to pass and use other parameters in the templates.  

In the `base.html` in (myproject/templates/layout.html) file we can change this line `<a href="/posts">` to this:  

```html
...
	<a href="{% url 'posts' %}">Posts</a>
...
```

..`{% url 'posts' %}` is a template tag that will refer to the  the URL pattern with the name `posts`.  

#### About path converters:  

Django provides a number of path converters that can be used to match different types of URL patterns.  
More about this [here](https://docs.djangoproject.com/en/5.0/topics/http/urls/)  

This is from the docs:  
```
The following path converters are available by default:  
slug - Matches any slug string consisting of ASCII letters or numbers, plus the hyphen and underscore characters. For example, building-your-1st-django-site.  
...
```

Back to our `urls.py` file in the app folder (`myproject/posts/urls.py`) we can add a new URL pattern that will render a specific post based on the `slug` of the post:  

```python
from django.urls import path
from . import views

app_name = 'posts' # this is a namespace for the URL patterns

urlpatterns = [
	path('', views.posts_list, name='posts_list'),
	path('<slug:slug>/', views.post_page, name='page'), # this is a dynamic URL pattern that will match any URL that contains a slug parameter
]
```
..`app_name = 'posts'` is a namespace for the URL patterns, so it is easier to refer / identify the names of URL patterns used in the templates!!   
After this we need to update the `layout.html` file in the `myproject/templates` folder to include the link to the specific post. Instead of the `list` url we specify `posts:list` ..:  

```html
...
	<a href="{% url 'posts:list' slug=post.slug %}">{{ post.title }}</a>
...
``` 

After this we need to add a new view function `post_page` to the `views.py` file in the app folder (`myproject/posts/views.py`):   
(this will be changed after we see that it is working)  

```python
from django.shortcuts import render
from .models import Post
from django.http import HttpResponse

# Create your views here.
def posts_list(request):
	posts = Post.objects.all().order_by('-date')
	return render(request, 'posts/posts_list.html', { 'posts': posts })

def post_page(request, slug):
	return HttpResponse(slug)
```

Also we change the `posts_list.html` file in the `myproject/posts/templates/posts` folder to include the links to the specific posts:  

```html
{% extends "layout.html" %}
{% block title %}
	<title>Posts</title>
{% endblock %}
{% block content %}
	<h1>posts</h1>
	{% for post in posts %}
		<h2>
			<a href="{% url 'posts:page' slug=post.slug %}">
				{{ post.title }}
			</a>
		</h2>
		<p>{{ post.date }}</p>
		<p>{{ post.body }}</p>
	{% endfor %}
{% endblock %}
```
..`{% url 'posts:page' slug=post.slug %}` is a template tag that will refer to the URL pattern with the name `page` and pass the `slug` parameter to the URL pattern.  
`.. posts:page` is a specified namespace for the URL pattern.  
Now when we click on the post title in the browser it will render the `slug` of the post.  

To render the specific post we need to update the `post_page` view function in the `views.py` file in the app folder (`myproject/posts/views.py`):  

```python
from django.shortcuts import render
from .models import Post

# Create your views here.
def posts_list(request):
	posts = Post.objects.all().order_by('-date') # this will return all the posts (-date will order the posts by date in descending order by date)
	return render(request, 'posts/posts_list.html', { 'posts': posts }) # this will render the request to the template posts_list.html

def post_page(request, slug):
	post = Post.objects.get(slug=slug) # this will get the post with the slug that matches the slug in the url
	return render(request, 'posts/post_page.html', { 'post': post }) # this will render the request to the template post_page.html
```

Right after this we will add a new template `post_page.html` in the `myproject/posts/templates/posts` folder to render the specific post:  

```html
{% extends "layout.html" %}

{% block title %}
	{{ post.title }}
{% endblock %}

{% block content %}
	<section>
		<h1>{{ post.title }}</h1>	
		<p>{{ post.date }}</p>
		<p>{{ post.body }}</p>
	</section>
{% endblock %}
```

Now when we click on the post title in the browser it will render the specific post with the title, date and body of the post on the separate page.  

## ADDING IMAGES:

In `settings.py` (in `myproject/myproject/settings.py`) file we need to add the path to the `media` folder, which will be used to store the images uploaded by the users:  

```python
...
MEDIA_URL = 'media/'

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
...
```

Then in the `urls.py` file in the project folder (`myproject/myproject/urls.py`) we need to add the following line to the `urlpatterns` list:  

```python
...
from djngo.conf.urls.static import static # this is used to serve the static files
from django.conf import settings # this is used to access the settings

...
...
# Add media url to urlpatterns to tell django where to find them
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

```

Next is to add changes to the model in the `models.py` file in the app folder (`myproject/posts/models.py`):  
but before that in the terminal, virtual environment should be activated and we install `Pillow` package:  

`pip install Pillow` - to install Pillow package.  
*Pillow is a Python Imaging Library (PIL) that adds image processing capabilities to Python interpreter. It supports formats (jpeg, png, bmp, gif, ppm, tiff). Available features like cropping, resizing, color manipulation.*

```python
...
from django.db import models

# Create your models here.
class Post(models.Model):
... # add the following line to the model:
	banner = models.ImageField(default='default.jpg', blank=True) # this wont work withoul pillow installed !!
...
```

For the changes to take effect we need to run migrations:  
`python manage.py makemigrations` - to create new migrations based on the changes made to the cusom models, created by the user.  
`python manage.py migrate` - to apply the new migrations to the database.  

After running the server `python manage.py runserver` we can go to the admin panel, see the new field `banner` in the `Post` model and we also can upload the image for the post.  
This will automatically create a new folder `media` in the root of the project folder and store the uploaded images there.  

The last thing to add is to update the `post_page.html` file in the `myproject/posts/templates/posts` folder to render the image of the post:  

```html
{% extends "layout.html" %}

{% block title %}
	{{ post.title }}
{% endblock %}

{% block content %}
	<section>
		<img 
			class="banner"
			src="{{ post.banner.url }}" 
			alt="{{ post.title }}"
		/>
		<h1>{{ post.title }}</h1>	
		<p>{{ post.date }}</p>
		<p>{{ post.body }}</p>
	</section>
{% endblock %}
```
..here we have added the `<img..>` tag that will render the image of the post.  

## ADDING USERS APP:

1) 
As a recap what was done to creat4e `posts` app. We created a new app `users`:
`python manage.py startapp users` - to create a new app (users here is a name for a new django app).  

After this we need to add the `users` app to the `INSTALLED_APPS` list in the `settings.py` file of the `myproject` folder (`myproject/myproject/settings.py`):  

```python
...
INSTALLED_APPS = [
	...
	'posts', # this is the app we created before
	'users',
]
```

2) 
Next step is to add the `urls.py` file in the app folder (`myproject/users/urls.py`), which is similar to the `urls.py` file in the `posts` app folder with slight changes:  

```python
from django.urls import path
from . import views

app_name = 'users'

urlpatterns = [
	path('register/', views.register_view, name="register"),
]
```
..`app_name = 'users'` is a namespace for the URL patterns, so it is easier to refer / identify the names of URL patterns used in the templates!!  

3) 
After this we also need to change the `urls.py` file in the project folder (`myproject/myproject/urls.py`) to include the URL patterns from the `users` app:  

```python
...
urlpatterns = [
    path('admin/', admin.site.urls),
	path('', views.homepage),
	path('about/', views.about),
	path('posts/', include('posts.urls')),
	path('users/', include('users.urls')), # this is the new line that includes the URL patterns from the users app
]
```
..teh same way which was done for the `posts` app.  

4) 
Next step is to add the `views.py` file in the app folder, which will contain the view functions for the `users` app (`myproject/users/views.py`):  

```python
from django.shortcuts import render

# The following function/method is specified in the `urls.py` as the second argument
def register_view(request):
	return render(request, 'users/register.html')

```

This will render the `register.html` template when the user visits the `/users/register/` URL. Which we will create as next step.  

5) 
In the similr way (as with the `posts` app) we create a new directory `templates` in the `users` app folder and another directory `users` inside the `templates` directory (`myproject/users/templates/users`).  
This is where the `register.html` file will be created.  

The file will contain the form that the user will use to register on the website `register.html`:  

```html
{% extends "layout.html" %}

{% block title %}
	Register a New User
{% endblock %}

{% block content %}
	<section>
		<h1>Register a New User !</h1>	
	</section>
{% endblock %}
```
..nothing fancy, similar to the `post_page.html` file.  

After these steps we can run the server `python manage.py runserver` and visit the `../users/register/` URL to see the form that the user will use to register on the website.  

We dont have the proper link to that page yet and we also need to add the registration functionality to the form.  

This woll be done next.  

## REGISTRATION FORM:  

1) 


(01:50:00)  


