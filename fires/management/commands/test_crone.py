from django.core.management.base import BaseCommand, CommandError
from datetime import datetime


class Command(BaseCommand):

    def handle(self, *args, **options):
        f = open('/tmp/crome_test', 'a+')
        f.write(str(datetime.now()) + '\n')
        f.close()
