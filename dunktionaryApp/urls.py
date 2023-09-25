from django.urls import path
from .views import indexPageView, dunkPageView, passPageView, passLibPageView, dunkLibPageView, searchPageView, trainPageView, theoryPageView

urlpatterns = [
    path('', indexPageView, name = "index"),
    path('MakeATrain/', trainPageView, name= "makeATrain"),
    path('Theory/', theoryPageView, name= "dunkTheory"),
    path('Search/', searchPageView, name= "search"),
    path('Passes/', passLibPageView, name = "passlib"),
    path('Passes/<pass_altName>/', passPageView, name = "pass_altName"),
    path('Dunks/', dunkLibPageView, name = "dunklib"),
    path('Dunks/<dunk_altName>/', dunkPageView, name = "dunk_altName")
]
