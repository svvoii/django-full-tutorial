from django.urls import path
from . import views

app_name = 'users'

# the second argument has to be a function / method from views.py for this app
urlpatterns = [
	path('register/', views.register_view, name="register"),
]
