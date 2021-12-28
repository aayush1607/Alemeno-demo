from django.contrib import admin
from .models import *

admin.site.register(Kid,KidAdmin)
admin.site.register(Image,ImageAdmin)

