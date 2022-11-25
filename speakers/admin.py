from django.contrib import admin
from .models import Speaker, Manufacturer, Comment, SpeakerUser

# Register your models here.

admin.site.register(Speaker)
admin.site.register(Manufacturer)
admin.site.register(Comment)
admin.site.register(SpeakerUser)