from django.db import models

class EmissionCap(models.Model):
    emission_limit = models.IntegerField()
    duration = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        duration_str = str(self.duration)
        return f"The emission limit for {self.duration} is {self.emission_limit}"
