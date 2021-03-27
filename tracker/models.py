from django.db import models

class Squirrel(models.Model):

    X = models.FloatField()
    Y = models.FloatField()
    Unique_Squirrel_ID = models.CharField(max_length = 50)
    Hectare_Choices = [('AM','AM'),('PM','PM'),]
    Hectare = models.CharField(max_length = 10, choices = Hectare_Choices)
    Shift = models.CharField(max_length = 10)
    Date = models.IntegerField()
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
    Running_Choices = [('TRUE','TRUE'),('FALSE','FALSE'),]
    Running = models.CharField(max_length = 10, choices = Running_Choices)
    Chasing = models.CharField(max_length = 10, choices = Running_Choices)
    Climbing = models.CharField(max_length = 10, choices = Running_Choices)
    Eating = models.CharField(max_length = 10, choices = Running_Choices)
    Foraging = models.CharField(max_length = 10, choices = Running_Choices)
    Other_Activities = models.CharField(max_length = 30, blank = True)
    Kuks = models.CharField(max_length = 10, choices = Running_Choices)
    Quaas = models.CharField(max_length = 10, choices = Running_Choices)
    Moans = models.CharField(max_length = 10, choices = Running_Choices)
    Tail_flags = models.CharField(max_length = 10, choices = Running_Choices)
    Tail_twitches = models.CharField(max_length = 10, choices = Running_Choices)
    Approaches = models.CharField(max_length = 10, choices = Running_Choices)
    Indifferent = models.CharField(max_length = 10, choices = Running_Choices)
    Runs_from = models.CharField(max_length = 10, choices = Running_Choices)
    Other_Interactions = models.CharField(max_length = 40, blank = True)
    Lat_Long = models.CharField(max_length = 80)

    def __str__(self):
        return self.Unique_Squirrel_ID

