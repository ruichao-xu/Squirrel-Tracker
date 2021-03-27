from django.db import models
from datetime import datetime
from django.utils import timezone

class Squirrel(models.Model):

    X = models.FloatField()
    Y = models.FloatField()
    Unique_Squirrel_ID = models.CharField(max_length = 50)
    Hectare_Choices = [('AM','AM'),('PM','PM'),]
    Hectare = models.CharField(max_length = 10, choices = Hectare_Choices)
    Shift = models.CharField(max_length = 10)
    Date = models.DateTimeField(default=timezone.now)
    Hectare_Squirrel_Number = models.IntegerField()
    Age_Choices = [('Adult','Adult'),('Juvenile','Juvenile'),]
    Age = models.CharField(max_length = 20, choices = Age_Choices, blank = True)
    Fur_Choices = [('Gray','Gray'),('Cinnamon','Cinnamon'),('Black','Black'),]
    Primary_Fur_Color = models.CharField(max_length=20, choices = Fur_Choices, blank = True)
    Combination_of_Primary_and_Highlight_Color = models.CharField(max_length=40)
    Color_notes = models.CharField(max_length = 60, blank = True)
    Location = models.CharField(max_length = 30)
    Above_Ground_Sighter_Measurement = models.CharField(max_length = 10)
    Specific_Location = models.CharField(max_length = 40)
    Running = models.BooleanField()
    Chasing = models.BooleanField()
    Climbing = models.BooleanField()
    Eating = models.BooleanField()
    Foraging = models.BooleanField()
    Other_Activities = models.CharField(max_length = 30, blank = True)
    Kuks = models.BooleanField()
    Quaas = models.BooleanField()
    Moans = models.BooleanField()
    Tail_flags = models.BooleanField()
    Tail_twitches = models.BooleanField()
    Approaches = models.BooleanField()
    Indifferent = models.BooleanField()
    Runs_from = models.BooleanField()
    Other_Interactions = models.CharField(max_length = 40, blank = True)
    Lat_Long = models.CharField(max_length = 80)

    def __str__(self):
        return f"ID: {self.Unique_Squirrel_ID} Date: {self.Date}"
