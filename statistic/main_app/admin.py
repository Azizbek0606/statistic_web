from django.db import models
from django.contrib.auth.models import User


class Activity_category(models.Model):
    category_name = models.CharField(max_length=150)
    
    def __str__ (self):
        return str(self.category_name)
