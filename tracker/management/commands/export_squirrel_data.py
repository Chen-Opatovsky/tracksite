from django.core.management.base import BaseCommand,CommandError

class Command(BaseCommand):
    help='Export CSV'

    def add_arguments(self,path):
        path.add_argument('csv_file',nargs='+',type=str)

    def handle(self,*arg,**options):
        import csv
        from django.http import HttpResponse

        def some_view(request):
            response = HttpResponse(content_type='text/csv')
            response['Content-Disposition'] = 'attachment; filename="csv_file.csv"'
            writer = csv.writer(response)
            print(response)
            writer.writerow()
            return response

