from tkinter import Image
from django.contrib import admin
from .models import Like, Profile, Comments

# Register your models here.
admin.site.register(Profile)
admin.site.register(Like)
admin.site.register(Comments)

