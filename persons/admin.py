from django.contrib import admin
from .models import Persons, Skills, Position

class PersonsAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'age', 'position')
    search_fields = ('first_name', 'last_name', 'skills__name', 'position__name')
    list_filter = ('age', 'position', 'skills')
    filter_horizontal = ('skills',)

admin.site.register(Persons, PersonsAdmin)
admin.site.register(Skills)
admin.site.register(Position)
