from django.shortcuts import render
from .models import Post

# Create your views here.
def posts_list(request):
	posts = Post.objects.all().order_by('-date') # this will return all the posts (-date will order the posts by date in descending order by date)
	return render(request, 'posts/posts_list.html', { 'posts': posts }) # this will render the request to the template posts_list.html

def post_page(request, slug):
	post = Post.objects.get(slug=slug) # this will get the post with the slug that matches the slug in the url
	return render(request, 'posts/post_page.html', { 'post': post }) # this will render the request to the template post_page.html
	
