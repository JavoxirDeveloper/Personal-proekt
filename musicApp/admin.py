from django.contrib import admin
from .models import Album, Singer, Music
# Register your models here.


admin.site.register(Music)
admin.site.register(Singer)
admin.site.register(Album)