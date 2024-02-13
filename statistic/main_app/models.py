from django.db import models
from datetime import timedelta


class Habits_category(models.Model):
    category_name = models.CharField(max_length=150)

    def __str__(self):
        return str(self.category_name)


from django.db import models


class Daily_Works(models.Model):
    name = models.CharField(max_length=150)
    day_work = models.DateTimeField(auto_now_add=True)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    works_category = models.ForeignKey(
        Habits_category,
        on_delete=models.CASCADE,
        related_name="daily_works",
    )
    workduration = models.DurationField(default=timedelta())

    def save(self, *args, **kwargs):
        self.workduration = self.end_time - self.start_time
        super(Daily_Works, self).save(*args, **kwargs)
