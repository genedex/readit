from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Book(models.Model):
	title = models.CharField(max_length = 255)
	author = models.CharField(max_length = 255)
	review = models.TextField(blank=True, null=True)
	date_reviewd = models.DateTimeField(blank=True, null=True)
	is_favorite = models.BooleanField(default=False)
