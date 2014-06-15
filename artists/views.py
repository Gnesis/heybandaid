import json

from django.shortcuts import render
from django.template.defaultfilters import slugify
from django.http import HttpResponseRedirect

from django.http import HttpResponseBadRequest
from django.http import HttpResponse
from artists.models import Artist
from artists.forms import ArtistForm, ConcertForm


# Create your views here.
def artist(request, slug=''):
	if slug == 'signup':
		return HttpResponseRedirect('signup/')
	try:
		slug = slugify(slug)
		artist = Artist.objects.get(slug=slug)
		context = { 'artist': artist }
	except:
		context = { 'error': 'not found', 'msg': 'you can\'t always get what you want'}

	return render(request, 'artist/index.html', context)

def signup(request):
  if request.method == 'POST':
    form = ArtistForm(request.POST, request.FILES)
    if form.is_valid():
      newartist = form.save(commit=False)
      newartist.name = request.POST['name']
      newartist.email = request.POST['email']
      newartist.password = request.POST['password']
      newartist.slug = slugify(request.POST['name'])
      newartist.photo = request.FILES['photo']
      newartist.description = request.POST['description']
      newartist.save()

      # Solo ejecuta con JQuery Request
      if request.is_ajax():
        return HttpResponse('OK')
      else:
        # Render para forma sin AJAX
				pass
    else:
      if request.is_ajax():
      # JSON for parsing
        errors_dict = {}
        if form.errors:
          for error in form.errors:
            e = form.errors[error]
            errors_dict[error] = unicode(e)
          return HttpResponseBadRequest(json.dumps(errors_dict))
        else:
          # render() form with errors (No AJAX)
          pass
  else:
    form = ArtistForm()

  return render(request, 'artist/register.html', {'form':form})

def add_concert( request ):
  if request.method == 'POST':
    form = ConcertForm(request.POST, request.FILES)
  else:
    form = ConcertForm()
  return render(request, 'artist/concert.html', {'form':form} )