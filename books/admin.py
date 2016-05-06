from django.contrib import admin

# Register your models here.
from .models import Book, Author


class BookAdmin(admin.ModelAdmin):
	fieldsets = [
	("Book Details",{"fields": ["title","authors"]}),
	("Review",{"fields":["is_favourite","review","date_reviewed"]})
	]


admin.site.register(Author)
admin.site.register(Book, BookAdmin)