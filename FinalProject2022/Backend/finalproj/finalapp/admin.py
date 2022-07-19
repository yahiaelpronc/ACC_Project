from django.contrib import admin
from .models import Myuser, Vet, locations, Messages
# Register your models here.
admin.site.register(Myuser)
admin.site.register(Vet)
admin.site.register(locations)
admin.site.register(Messages)
