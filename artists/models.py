from django.db import models
from markitup.fields import MarkupField
from django_autoslug.fields import AutoSlugField

# Create your models here.

class Artist(models.Model):
    name = models.CharField(max_length=60)
    email = models.CharField(max_length=60)
    password = models.CharField(max_length=8)
    #slug = AutoSlugField(populate_from=('name',), unique=True, max_length=255, overwrite=True)
    #photo = models.ImageField(upload_to='news')
    #description = MarkupField(blank=True, null=True)
    #created = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.name