from django.contrib import admin
from myapp.models import StatusModel

# Register your models here.
from .models import Album, Song, Author, Book, Vehicle, Car

admin.site.register(StatusModel)
# admin.site.register(GeeksModel)
admin.site.register(Album)
admin.site.register(Song)
admin.site.register(Author)
admin.site.register(Book)
admin.site.register(Vehicle)
admin.site.register(Car)