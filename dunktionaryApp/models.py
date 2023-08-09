from django.db import models
from django.db.models import Q



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


# class SearchResultsList(models.Model):
#    model = Dunk
#    context_object_name = "name"
#    template_name = "dunkApp/search2.html"

#    def get_queryset(self):
#       query = self.request.GET.get("q")
#       return Dunk.objects.filter(name__search=query)

                  # class Trick(models.Model):
                  #      name = models.CharField(max_length = 100, null=True, blank = True)
                  #      altName = models.CharField(max_length = 100, null=True, blank = True)
                  #      description = models.CharField(max_length = 250, null=True, blank = True)
                  #      image = models.CharField(max_length = 500, null=True, blank = True)
                  #      video = models.CharField(max_length = 500, null=True, blank = True)
                  #      dunker = models.CharField(max_length = 75, null=True, blank = True)
                  #      hierarchy = models.CharField(max_length = 250, null=True, blank = True)
                  #      prereq = models.CharField(max_length = 150, null=True, blank = True)
                  #      classification = models.OneToOneField("Classification",null=True, blank=True,on_delete=models.CASCADE)
                  #      type = models.OneToOneField("Type",null=True, blank=True,on_delete=models.CASCADE)
                     
                  #      def __str__(self):
                  #         return self.name

                  #      class Meta:
                  #         db_table = "tricks"

                  # class Classification(models.Model):
                  #    classification = models.CharField(max_length = 150, null=True, blank = True)

                  #    def __str__(self):
                  #       return self.classification

                  #    class Meta:
                  #       db_table = "classifications"

                  # class Type(models.Model):
                  #    type = models.CharField(max_length=100, null=True, blank=True)

                  #    def __str__(self):
                  #       return self.type

                  #    class Meta:
                  #       db_table = "types"
