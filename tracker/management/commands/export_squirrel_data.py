from django.core.management.base import BaseCommand,CommandError
from tracker.models import Sighting

class Command(BaseCommand):
    help='Export CSV'

    def add_arguments(self,path):
        path.add_argument('csv_file',nargs='+',type=str)

    def handle(self,*arg,**options):
        import csv
        from django.http import HttpResponse
        #writing header
        path=str(options['csv_file'][0])
        with open(path,'w') as f:
            writer = csv.writer(f)
            header=['latitude',
                    'longitude',
                    'squirrel_id',
                    'shift',
                    'date',
                    'age',
                    'fur_color',
                    'location',
                    'specific_location',
                    'running',
                    'chasing',
                    'climbing',
                    'eating',
                    'foraging',
                    'other_activities',
                    'kuks',
                    'quaas',
                    'moans',
                    'tail_flags',
                    'tail_twitches',
                    'approaches',
                    'indifferent',
                    'runs_from',]
            writer.writerow(header)
            #writing data
            squirrel_data=Sighting.objects.all()
            for data in squirrel_data:
                writer.writerow([data.latitude,
                                 data.longitude,
                                 data.squirrel_id,
                                 data.shift,
                                 data.date,
                                 data.age,
                                 data.fur_color,
                                 data.location,
                                 data.specific_location,
                                 data.running,
                                 data.chasing,
                                 data.climbing,
                                 data.eating,
                                 data.foraging,
                                 data.other_activities,
                                 data.kuks,
                                 data.quaas,
                                 data.moans,
                                 data.tail_flags,
                                 data.tail_twitches,
                                 data.approaches,
                                 data.indifferent,
                                 data.runs_from,])

        
