from django.db import models
from django.contrib.auth.models import User # this will import the User model from django.contrib.auth.models

# Create your models here.
class Post(models.Model):
	title = models.CharField(max_length=100)
	body = models.TextField()
	slug = models.SlugField()
	date = models.DateTimeField(auto_now_add=True)
	banner = models.ImageField(default='default.jpeg', blank=True) # this wont work withoul pillow installed !!
	author = models.ForeignKey(User, on_delete=models.CASCADE, default=None) # this will create a foreign key to the User model (on_delete=models.CASCADE will delete the post if the user is deleted)

	def __str__(self):
		return self.title
