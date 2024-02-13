from django.db import models

class Habits_category(models.Model):
    category_name = models.CharField(max_length=150)
    
    def __str__ (self):
        return str(self.category_name)