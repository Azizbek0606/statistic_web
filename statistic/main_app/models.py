from django.db import models
from datetime import timedelta


class Daily_Works(models.Model):
    HABITS_CATEGORY = (
        ("GOOD", "Good"),
        ("BAD", "Bad"),
        ("DAILY", "Daily"),
    )
    name = models.CharField(max_length=150)
    day_work = models.DateTimeField(auto_now_add=True)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    works_category = models.CharField(max_length=150, choices=HABITS_CATEGORY)
    workduration = models.DurationField(default=timedelta())

    def save(self, *args, **kwargs):
        self.workduration = self.end_time - self.start_time
        super(Daily_Works, self).save(*args, **kwargs)

    def __str__(self) -> str:
        return str(self.name)


class Spend_money(models.Model):
    why = models.CharField(max_length=150)
    how_much = models.CharField(max_length=150)
    which_day = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.why)
