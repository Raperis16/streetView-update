from django.db import models

# Create your models here.

class Random(models.Model):
    lng = models.FloatField(blank=False)
    lat = models.FloatField(blank=False) 
    nos = models.CharField(max_length = 50)
    def __str__(self):
        return str(self.id)
    # def __getitem__(self,key):
    #     print ("Inside `__getitem__` method!")
    #     return getattr(self,key)



class Game(models.Model):
    id_loc = models.ForeignKey(Random, on_delete=models.CASCADE, null=True, blank=True)
    Results = (
        ('Y', 'Yes'),
        ('N', 'No'),
    )
    Result = models.CharField(max_length = 1, choices = Results, null=True, blank=True)
    Fake1 = models.ForeignKey(Random, related_name='Fake1', on_delete=models.CASCADE, null=True, blank=True)
    Fake2 = models.ForeignKey(Random, related_name='Fake2', on_delete=models.CASCADE, null=True, blank=True)
    Fake3 = models.ForeignKey(Random, related_name='Fake3', on_delete=models.CASCADE, null=True, blank=True)
    def __str__(self):
        return str(self.id)

import time
class TimeGameMode(models.Model):
    now = time.time()
    future = now + 70
    if time.time() > future:
        print()

class timeResults(models.Model):
    username = models.CharField(max_length = 16,)
            