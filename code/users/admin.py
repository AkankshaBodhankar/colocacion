from django.contrib import admin
from .models import *

admin.site.register(Jobs)
admin.site.register(JobsApplied)
admin.site.register(Tests)
admin.site.register(Questions)
admin.site.register(TestsTaken)
admin.site.register(Choice)