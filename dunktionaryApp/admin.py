from django.contrib import admin
from .models import Dunk, Pass, Variation, PassLevel, DunkLevel, TrickScore



class FilterPass(admin.ModelAdmin):
    list_display = ("name", "image", "video", "dunker", "prereq")
    list_filter = ("dunker",)

class FilterDunk(admin.ModelAdmin):
    list_display = ("name", "image", "video", "dunker", "prereq")
    list_filter = ("dunker",)
    
class VariationAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)

class PassLevelAdmin(admin.ModelAdmin):
    list_display = ("pass_ref", "level", "can_start", "can_follow", "variations",)
    list_filter = ("level", "can_start", "can_follow", "pass_ref__name",)
    search_fields = ("pass_ref__name",)
    filter_horizontal = ("variations",)

class DunkLevelAdmin(admin.ModelAdmin):
    list_display = ("dunk_ref", "level", "variations",)
    list_filter = ("level",)
    search_fields = ("dunk_ref__name",)
    filter_horizontal = ("variations",)

class TrickScoreAdmin(admin.ModelAdmin):
    list_display = ("trick_name", "score_value")
    search_fields = ("trick_name",)

admin.site.register(Dunk, FilterDunk)
admin.site.register(Pass, FilterPass)
admin.site.register(Variation, VariationAdmin)
admin.site.register(PassLevel, PassLevelAdmin)
admin.site.register(DunkLevel, DunkLevelAdmin)
admin.site.register(TrickScore, TrickScoreAdmin)