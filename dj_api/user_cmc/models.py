from django.db import models
import uuid

# Create your models here.

class Member(models.Model):
    id = models.CharField(primary_key=True, editable=False, max_length=8)
    real_name = models.CharField(max_length=100)
    tz = models.CharField(max_length=50)

    def __str__(self):
        return self.id

    @property
    def activity_periods(self):
        return self.activityperiods_set.all().order_by('start_time')


class ActivityPeriods(models.Model):
    member =  models.ForeignKey(Member, on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

    