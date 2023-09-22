from django.db import models
from datetime import date

# Create your models here.



class Limit(models.Model):
    emission_limit = models.IntegerField()
    duration = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return f"The emission limit for ${self.duration} is ${self.emission_limit}"
        
