from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Book(models.Model):
	title = models.CharField(max_length = 255, verbose_name = "Book's title")
	author = models.CharField(max_length = 25, help_text = "Use pen name, not real name!")
	review = models.TextField(blank=True, null=True)
	date_reviewd = models.DateTimeField(blank=True, null=True)
	is_favorite = models.BooleanField(default=False, verbose_name = "Favourite?")

	def __str__(self):
		return self.title