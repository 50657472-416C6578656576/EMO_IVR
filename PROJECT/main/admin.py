from django.contrib import admin
from .models import Competition, Sportsman, Team


admin.site.register(Competition)
admin.site.register(Team)
admin.site.register(Sportsman)