import csv
from django.core.management.base import BaseCommand
from tracker.models import Squirrel

class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('csv_file')

    def handle(self, *args, **options):
        with open(options['csv_file'],'w', newline='') as fp:
            writer = csv.writer(fp)


            writer.writerow(['X','Y','Unique Squirrel ID','Hectare','Shift','Date','Hectare Squirrel Number','Age','Primary Fur Color', 'Highlight Fur Color','Combination of Primary and Highlight Color','Color notes','Location','Above Ground Sighter Measurement','Specific Location','Running','Chasing','Climbing','Eating','Foraging','Other Activities','Kuks','Quaas','Moans','Tail flags','Tail twitches','Approaches','Indifferent','Runs from','Other Interactions','Lat/Long'])

            for squirrel in Squirrel.objects.all().values_list('X','Y','Unique_Squirrel_ID','Hectare','Shift','Date','Hectare_Squirrel_Number','Age','Primary_Fur_Color','Highlight_Fur_Color','Combination_of_Primary_and_Highlight_Color','Color_notes','Location','Above_Ground_Sighter_Measurement','Specific_Location','Running','Chasing','Climbing','Eating','Foraging','Other_Activities','Kuks','Quaas','Moans','Tail_flags','Tail_twitches','Approaches','Indifferent','Runs_from','Other_Interactions','Lat_Long'):
                writer.writerow(squirrel)
