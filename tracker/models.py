from django.db import models

class Squirrel_csv(models.Model):
    X = models.FloatField()
    Y = models.FloatField()
    Unique-Squirrel-ID = models.CharField(max_length = 50)
    Hectare = models.CharField(max_length = 10)
    Shift = models.CharField(max_length = 10)
    Date = models.IntegerField()
    Hectare-Squirrel-Number = models.IntegerField()
    Age_Choices = [(Adult),(Juvenile),]
    Age = models.CharField(max_length = 20, choices = Age_Choices, blank = True)
    Fur_Choices = [(Gray),(Cinnamon),(Black),]
    Primary-Fur-Color = models.CharField(max_length=20, choices = Fur_Choices, blank = True)
    Combination-of-Primary-and-Highlight-Color = models.CharField(max_length=40)
    Color-notes = models.CharField(max_length = 60, blank = True)
    Location = models.CharField(max_length = 30)
    Above-Ground-Sighter-Measurement = models.CharField(max_length = 10)
    Specific-Location = models.CharField(max_length = 40)
    Running_Choices = [(TRUE),(FALSE),]
    Running = models.CharField(max_length = 10, choices = Running_Choices)
    Chasing = models.CharField(max_length = 10, choices = Running_Choices)
    Climbing = models.CharField(max_length = 10, choices = Running_Choices)
    Eating = models.CharField(max_length = 10, choices = Running_Choices)
    Foraging = models.CharField(max_length = 10, choices = Running_Choices)
    Other-Activities = models.CharField(max_length = 30, blank = True)
    Kuks = models.CharField(max_length = 10, choices = Running_Choices)
    Quaas = models.CharField(max_length = 10, choices = Running_Choices)
    Moans = models.CharField(max_length = 10, choices = Running_Choices)
    Tail-flags = models.CharField(max_length = 10, choices = Running_Choices)
    Tail-twitches = models.CharField(max_length = 10, choices = Running_Choices)
    Approaches = models.CharField(max_length = 10, choices = Running_Choices)
    Indifferent = models.CharField(max_length = 10, choices = Running_Choices)
    Runs-from = models.CharField(max_length = 10, choices = Running_Choices)
    Other-Interactions = models.CharField(max_length = 40, blank = True)
    Lat/Long = models.CharField(max_length = 80)
