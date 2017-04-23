
# Full path and name to your csv file
csv_filepathname="C:/users/akanksha bodhankar/Desktop/job.csv"
# Full path to your django project directory
your_djangoproject_home="D:/btechproject/colocacion/"

import sys,os
sys.path.append(your_djangoproject_home)
os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'

import django
django.setup()
from jobs.models import *
from decimal import Decimal
import ast


import csv
dataReader = csv.reader(open(csv_filepathname), delimiter=',', quotechar='"')

with open(csv_filepathname) as f:
    reader = csv.reader(f)
    for row in reader:
        _, created = Jobs.objects.get_or_create(
                job_role=row[5],
                job_title=row[0],
                job_type=row[3],
                experience_required=row[8],
                company_name=row[4],
                salary=row[6],
                location=row[2],
                skills_set=row[9],
                job_class=row[7],
                desc=row[1],
        )

