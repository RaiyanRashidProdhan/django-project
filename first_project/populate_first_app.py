import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','first_project.settings')

import django
django.setup()

#FAKE POPULATION SCRIPT
import random
from first_app.models import AccessRecord,Topic,Webpage
from faker import Faker

fakegen = Faker()
topic = ['Search', 'Social Media', 'Marketplace', 'News', 'Games']

def add_topic():
    t = Topic.objects.get_or_create(top_name=random.choice(topic))[0]
    t.save()
    return t

def populate(N=5):
    for entry in range(N):
        #GET THE TOPIC FOR THE ENTRIES
        top = add_topic()
        #CREATE FAKE DATA FOR THE ENTRIES
        fake_url = fakegen.url()
        fake_date = fakegen.date()
        fake_name = fakegen.company()
        #CREATE THE NEW WEBPAGE ENTRIES
        webpg = Webpage.objects.get_or_create(topic=top,url=fake_url,name=fake_name)[0]
        #CREATE A FAKE ACCESS RECORD FOR THE Webpage
        acc_rec = AccessRecord.objects.get_or_create(name=webpg,date=fake_date)[0]

if __name__ == '__main__':
    print("Populating Script")
    populate(20)
    print("Populating Complete!")
