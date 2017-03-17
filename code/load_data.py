
# Full path and name to your csv file
csv_filepathname="C:/users/akanksha bodhankar/Downloads/details.csv"
# Full path to your django project directory
your_djangoproject_home="D:/btechproject/colocacion/"

import sys,os
sys.path.append(your_djangoproject_home)
os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'

import django
django.setup()
from accounts.models import *
from decimal import Decimal
import ast


import csv
dataReader = csv.reader(open(csv_filepathname), delimiter=',', quotechar='"')

with open(csv_filepathname) as f:
    reader = csv.reader(f)
    for row in reader:
        _, created = UserDetails.objects.get_or_create(
            email=row[1],
            name=row[2],
            password=row[2],
            city=row[3],
            mobile_num=row[4],
        )

with open(csv_filepathname) as f:
    reader = csv.reader(f)
    for row in reader:
        _, created = UserProfile.objects.get_or_create(
	        	email=row[1],
	            college_name=row[5],
	            branch=row[6],
	            degree=row[7],
	            degree_percent=row[13],
	            inter_percent=row[9],
	            ssc_percent=row[10],
	            skills=row[11],
	            interests=row[12],
        )