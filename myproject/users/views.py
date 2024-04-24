from django.shortcuts import render

# The following function is specified in the `urls.py` as the second argument
def register_view(request):
	return render(request, 'users/register.html')
