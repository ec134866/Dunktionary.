from django.urls import path
from .views import indexPageView, dunkPageView, passPageView, passLibPageView, dunkLibPageView, searchPageView, search2PageView, trainPageView

urlpatterns = [
    path('', indexPageView, name = "index"),
    path('MakeATrain/', trainPageView, name= "makeATrain"),
    path('Search/', searchPageView, name= "search"),
    path('search2/', search2PageView, name="search2"),
    path('Passes/', passLibPageView, name = "passlib"),
    path('Passes/<pass_altName>/', passPageView, name = "pass_altName"),
    path('Dunks/', dunkLibPageView, name = "dunklib"),
    path('Dunks/<dunk_altName>/', dunkPageView, name = "dunk_altName")
]
