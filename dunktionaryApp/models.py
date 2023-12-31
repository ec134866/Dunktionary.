from django.db import models
from django.db.models import Q
from django.contrib.postgres.search import SearchVector, SearchQuery


class Dunk(models.Model):
     name = models.CharField(max_length = 100, null=True, blank = True)
     altName = models.CharField(max_length = 100, null=True, blank = True)
     description = models.CharField(max_length = 250, null=True, blank = True)
     image = models.CharField(max_length = 500, null=True, blank = True)
     video = models.CharField(max_length = 500, null=True, blank = True)
     dunker = models.CharField(max_length = 75, null=True, blank = True)
     hierarchy = models.CharField(max_length = 250, null=True, blank = True)
     prereq = models.CharField(max_length = 150, null=True, blank = True)
   #   pqAltName = models.CharField(max_length = 150, null=True, blank = True)
     classification = models.CharField(max_length = 150, null=True, blank = True)
   
     
     def __str__(self):
        return self.name

     class Meta:
        db_table = "dunks"

class Pass(models.Model):
     name = models.CharField(max_length = 100, null=True, blank = True)
     altName = models.CharField(max_length = 100, null=True, blank = True)
     description = models.CharField(max_length = 250, null=True, blank = True)
     image = models.CharField(max_length = 500, null=True, blank = True)
     video = models.CharField(max_length = 500, null=True, blank = True)
     dunker = models.CharField(max_length = 75, null=True, blank = True)
     hierarchy = models.CharField(max_length = 250, null=True, blank = True)
     prereq = models.CharField(max_length = 150, null=True, blank = True)
   #   pqAltName = models.CharField(max_length = 150, null=True, blank = True)
     classification = models.CharField(max_length = 150, null=True, blank = True)
     type = models.CharField(max_length=100, null=True, blank=True)

     def __str__(self):
        return self.name

     class Meta:
        db_table = "passes"
