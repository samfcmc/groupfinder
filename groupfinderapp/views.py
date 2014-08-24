from django.shortcuts import render

# Create your views here.
def index(request):
	context = {'test': 'a simple string'}
	return render(request, 'base.html', context)

