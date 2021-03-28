from django.forms import ModelForm
from .models import Squirrel

class AddSightingsForm(ModelForm):
    class Meta:
        model = Squirrel
        fields = [
                'X',
                'Y',
                'Unique_Squirrel_ID',
                'Shift',
                'Date'
        ]

class UpdateForm(ModelForm):
    class Meta:
        model = Squirrel
        fields = [
                'X',
                'Y',
                'Unique_Squirrel_ID',
                'Shift',
                'Date',
                'Age'
                ]

