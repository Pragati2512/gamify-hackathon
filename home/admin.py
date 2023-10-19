from django.contrib import admin
from .models import person, goals, badge, bp_track

admin.site.register(person)
admin.site.register(goals)
admin.site.register(badge)
admin.site.register(bp_track)