from django.core.management.base import BaseCommand, CommandError

from random import randrange
from datetime import timedelta, datetime
import uuid
from user_cmc.models import *
from faker import Faker


class Command(BaseCommand):
    help = 'Command for creating members'


    def handle(self, *args, **options):
        
        fake = Faker()
        for _ in range(3):
            mid = str(uuid.uuid4())
            mid = mid.upper()
            mid = mid.replace("-","")

            id = mid[0:8]
            real_name = fake.name()
            tz = fake.timezone()

            # print(id, real_name, tz)
            member = Member.objects.get_or_create(id = id, real_name=real_name, tz=tz)

            for __ in range(3):
                # print(fake.date_time())
                start = datetime.strptime('1/1/2020 1:30 PM', '%m/%d/%Y %I:%M %p')
                end = datetime.strptime('7/3/2020 4:50 AM', '%m/%d/%Y %I:%M %p')

                delta = end - start
                int_delta = (delta.days * 24 * 60 * 60) + delta.seconds
                random_second = randrange(int_delta)

                start_time = start + timedelta(seconds=random_second)
                end_time = start_time + timedelta(seconds=43200)

                member = Member.objects.get(id=id)

                ActivityPeriods.objects.get_or_create(member = member, start_time=start_time, end_time=end_time)
            

        return 'Members created Successfully'