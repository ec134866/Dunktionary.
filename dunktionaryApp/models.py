from django.db import models
from django.db.models import Q
from django.contrib.postgres.search import SearchVector, SearchQuery


class Dunk(models.Model):
     name = models.CharField(max_length = 100, null=True, blank = True)
     classification = models.CharField(max_length = 150, null=True, blank = True)
     altName = models.CharField(max_length = 100, null=True, blank = True)
     description = models.CharField(max_length = 250, null=True, blank = True)
     image = models.CharField(max_length = 500, null=True, blank = True)
     video = models.CharField(max_length = 500, null=True, blank = True)
     dunker = models.CharField(max_length = 75, null=True, blank = True)
     hierarchy = models.CharField(max_length = 250, null=True, blank = True)
     prereq = models.CharField(max_length = 150, null=True, blank = True)
     prereq_classification = models.CharField(max_length = 150, null=True, blank = True)
     
     def __str__(self):
        return self.name

     class Meta:
        db_table = "dunks"

class Pass(models.Model):
     name = models.CharField(max_length = 100, null=True, blank = True)
     classification = models.CharField(max_length = 150, null=True, blank = True)
     altName = models.CharField(max_length = 100, null=True, blank = True)
     description = models.CharField(max_length = 250, null=True, blank = True)
     image = models.CharField(max_length = 500, null=True, blank = True)
     video = models.CharField(max_length = 500, null=True, blank = True)
     dunker = models.CharField(max_length = 75, null=True, blank = True)
     hierarchy = models.CharField(max_length = 250, null=True, blank = True)
     prereq = models.CharField(max_length = 150, null=True, blank = True)
     prereq_classification = models.CharField(max_length = 150, null=True, blank = True)
     type = models.CharField(max_length=100, null=True, blank=True)

     def __str__(self):
        return self.name

     class Meta:
        db_table = "passes"

class Variation(models.Model):
    name = models.CharField(max_length=100, unique=True)
    
    class Meta:
        db_table = "variations"
        ordering = ['name']
    
    def __str__(self):
        return self.name

class PassLevel(models.Model):
    pass_ref = models.ForeignKey(Pass, on_delete=models.CASCADE, related_name='levels')
    level = models.IntegerField()
    can_start = models.BooleanField(default=False)
    can_follow = models.BooleanField(default=False)
    variations = models.ManyToManyField(Variation, blank=True, related_name='pass_levels')
    
    class Meta:
        db_table = "pass_levels"
        ordering = ['level', 'pass_ref__name']
    
    def __str__(self):
        flags = []
        if self.can_start:
            flags.append("start")
        if self.can_follow:
            flags.append("follow")
        flag_str = f" ({'/'.join(flags)})" if flags else ""
        return f"{self.pass_ref.name} - Level {self.level}{flag_str}"

class DunkLevel(models.Model):
    dunk_ref = models.ForeignKey(Dunk, on_delete=models.CASCADE, related_name='levels')
    level = models.IntegerField()
    variations = models.ManyToManyField(Variation, blank=True, related_name='dunk_levels')
    
    class Meta:
        db_table = "dunk_levels"
        ordering = ['level', 'dunk_ref__name']
    
    def __str__(self):
        return f"{self.dunk_ref.name} - Level {self.level}"

class TrickScore(models.Model):
    trick_name = models.CharField(max_length=250, unique=True, db_index=True)
    score_value = models.FloatField()
    
    class Meta:
        db_table = "trick_scores"
        ordering = ['trick_name']
    
    def __str__(self):
        return f"{self.trick_name}: {self.score_value}"