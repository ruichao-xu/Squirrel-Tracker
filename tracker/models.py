from django.db import models
from datetime import datetime
from django.utils import timezone

class Squirrel(models.Model):

    X = models.FloatField()
    Y = models.FloatField()
    Unique_Squirrel_ID = models.CharField(max_length = 50)
    Hectare_Choices = [('AM','AM'),('PM','PM'),]
    Hectare = models.CharField(max_length = 10, choices = Hectare_Choices, null = True, blank = True)
    Shift = models.CharField(max_length = 10)
    Date = models.DateTimeField(default=timezone.now)
    Hectare_Squirrel_Number = models.IntegerField(null = True, blank = True)
    Age_Choices = [('Adult','Adult'),('Juvenile','Juvenile'),]
    Age = models.CharField(max_length = 20, choices = Age_Choices, null = True, blank = True)
    Fur_Choices = [('Gray','Gray'),('Cinnamon','Cinnamon'),('Black','Black'),]
    Primary_Fur_Color = models.CharField(max_length=20, choices = Fur_Choices, null = True, blank = True)
    Combination_of_Primary_and_Highlight_Color = models.CharField(max_length=40,null = True, blank = True)
    Color_notes = models.CharField(max_length = 60, null = True, blank = True)
    Location = models.CharField(max_length = 30, null = True, blank = True)
    Above_Ground_Sighter_Measurement = models.CharField(max_length = 10, null = True, blank = True)
    Specific_Location = models.CharField(max_length = 40, null = True, blank = True)
    Running = models.BooleanField(null = True, blank = True)
    Chasing = models.BooleanField(null = True, blank = True)
    Climbing = models.BooleanField(null = True, blank = True)
    Eating = models.BooleanField(null = True, blank = True)
    Foraging = models.BooleanField(null = True, blank = True)
    Other_Activities = models.CharField(max_length = 30, null = True, blank = True)
    Kuks = models.BooleanField(null = True, blank = True)
    Quaas = models.BooleanField(null = True, blank = True)
    Moans = models.BooleanField(null = True, blank = True)
    Tail_flags = models.BooleanField(null = True, blank = True)
    Tail_twitches = models.BooleanField(null = True, blank = True)
    Approaches = models.BooleanField(null = True, blank = True)
    Indifferent = models.BooleanField(null = True, blank = True)
    Runs_from = models.BooleanField(null = True, blank = True)
    Other_Interactions = models.CharField(max_length = 40, null = True, blank = True)
    Lat_Long = models.CharField(max_length = 80, null = True, blank = True)


    def __str__(self):
        return f"ID: {self.Unique_Squirrel_ID} Date: {self.Date}"
