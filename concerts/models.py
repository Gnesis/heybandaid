from django.db import models
from markitup.fields import MarkupField
from django_autoslug.fields import AutoSlugField

from artists.models import Artist

# Create your models here.

class Concert(models.Model):
    name = models.CharField(max_length=60)
    artist = models.ForeignKey(Artist)
    slug = AutoSlugField(populate_from=('name',), unique=True, max_length=255, overwrite=True)
    poster = models.ImageField(upload_to='news', blank=True, null=True)
    budget = models.IntegerField(max_length=300)
    place = models.CharField(max_length=300, blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    description = MarkupField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.name

class Reward(models.Model):
	title = models.CharField(max_length=60)
	concert = models.ForeignKey(Concert)
	total = models.IntegerField(max_length=300)
	price = models.IntegerField(max_length=300)
	description = MarkupField(blank=True, null=True)
	created = models.DateTimeField(auto_now_add=True)

	def __unicode__(self):
		return self.title