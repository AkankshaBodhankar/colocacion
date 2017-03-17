from django.contrib import admin
from .models import *

admin.site.register(Tests)
admin.site.register(Questions)
admin.site.register(Choice)
admin.site.register(TestsTaken)
admin.site.register(Answers)
