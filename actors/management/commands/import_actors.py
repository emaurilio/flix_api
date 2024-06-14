import csv
from datetime import datetime
from django.core.management import BaseCommand
from django.core.management.base import CommandParser
from actors.models import Actor


class Command(BaseCommand):

    def add_arguments(self, parser: CommandParser):
        parser.add_argument(
            'file_name',
            type=str,
            help='nome do arquivo csv com atores',
        )

    def handle(self, *args, **options):
        file_name=options['file_name']

        with open(file_name,'r',encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                print(row['birthday'])
                name = row['name']
                birthday = datetime.strptime(row['birthday'],'%Y-%m-%d').date()
                nationality = row['nationality']

                self.stdout.write(self.style.NOTICE(name))
                self.stdout.write(self.style.NOTICE("'"+row['birthday']+"'"))

                Actor.objects.create(
                    name=name,
                    birthday=birthday,
                    nacionality=nationality,
                )

        self.stdout.write(self.style.SUCCESS('ATORES IMPORTADOS COM SUCESSO'))