from django.contrib import admin
from .models import Dunk, Pass




class Filter(admin.ModelAdmin):
    list_display = ("Image", "Video", "Dunker")
    list_filter = ("dunker")

admin.site.register(Dunk, Filter)
admin.site.register(Pass, Filter)