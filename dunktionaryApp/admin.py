from django.contrib import admin
from .models import Dunk, Pass



class FilterPass(admin.ModelAdmin):
    list_display = ("name", "image", "video", "dunker")
    list_filter = ("dunker",)

class FilterDunk(admin.ModelAdmin):
    list_display = ("name", "image", "video", "dunker")
    list_filter = ("dunker",)

admin.site.register(Dunk, FilterDunk)
admin.site.register(Pass, FilterPass)