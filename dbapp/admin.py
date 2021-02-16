from django.contrib import admin

# Register your models here.
from .models import Entry, Cmodel, Customer

admin.site.register(Entry)
admin.site.register(Cmodel)
admin.site.register(Customer)