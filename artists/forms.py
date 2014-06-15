from django import forms
from artists.models import Artist


class ArtistForm(forms.Form):
    name = forms.CharField(max_length=60)
    #slug = forms.CharField(max_length=60)
    email = forms.EmailField(max_length=60)
    password = forms.CharField(widget=forms.PasswordInput(), max_length=8)
    #photo = forms.ImageField(label='Selecciona una imagen', help_text='max. 2 megabytes')
    #description = forms.CharField(widget=forms.Textarea(), max_length=1000)
    #created = forms.CharField(max_length=60)

    class Meta:
    	model = Artist
    	fields = ['name', 'email', 'password', 'photo']
    	#exclude =['slug']
