from django.contrib import admin
from .models import Post
from .models import Patient
from .models import Doctor

admin.site.register(Post)
admin.site.register(Patient)
admin.site.register(Doctor)