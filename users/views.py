from django.shortcuts import render
from django.template.defaultfilters import slugify
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

# Create your views here.
def signup(request):
	if request.method == 'POST':
		formulario = UserCreationForm(request.POST)
		if formulario.is_valid():
			formulario.save()
			return HttpResponseRedirect('/')
	else:
		formulario = UserCreationForm()
	return render(request, 'user/nuevo_usuario.html', {'form':formulario})

def user(request, slug=''):
	if slug == 'signup':
		return HttpResponseRedirect('signup/')
	try:
		slug = slugify(slug)
		user = User.objects.get(slug=slug)
		context = { 'user': user }
	except:
		context = { 'error': 'not found', 'msg': 'you can\'t always get what you want'}

	return render(request, 'user/index.html', context)

def index(request):
	context = {}
	return render(request, 'index.html', context)
# def user(request):
# 	if slug == 'signup':
# 		return HttpResponseRedirect('signup/')
# 	try:
# 		slug = slugify(slug)
# 		username = User.objects.get(slug=slug)
# 		context = { 'user': username }
# 	except:
# 		context = { 'error': 'not found', 'msg': 'you can\'t always get what you want'}

# 	return render(request, 'user/index.html', context)
