from django.db import models

# Create your models here.
class InputDataModel(models.Model):
    area = models.FloatField()
    trans_floor = models.IntegerField()
    com_year = models.IntegerField()
    interest = models.FloatField()
    household = models.IntegerField()
    top_floor = models.IntegerField()
    subway_dist = models.FloatField()
    subway_cnt = models.IntegerField()
    bus_cnt = models.IntegerField()
    parking_lot = models.FloatField()
    school = models.IntegerField()
    hospital = models.IntegerField()