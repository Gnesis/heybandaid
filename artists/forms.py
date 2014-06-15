from django import forms
from artists.models import Artist
from concerts.models import Concert
from markitup.widgets import MarkItUpWidget

class ArtistForm(forms.ModelForm):
    name = forms.CharField(max_length=60)
    email = forms.EmailField(max_length=60)
    password = forms.CharField(widget=forms.PasswordInput(), max_length=8)
    photo = forms.ImageField(label='Selecciona una imagen', help_text='max. 2 megabytes')
    description = forms.CharField(widget=MarkItUpWidget())

    class Meta:
    	model = Artist

class ConcertForm(forms.ModelForm):
    name = forms.CharField(max_length=60)
    poster = forms.ImageField(label='Selecciona una imagen', help_text='max. 2 megabytes')
    budget = forms.CharField(max_length=60)
    place = forms.CharField(max_length=60)
    date = forms.CharField(max_length=60)
    description = forms.CharField(widget=MarkItUpWidget())

    class Meta:
        model = Concert