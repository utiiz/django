# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
from .models import *

# Register your models here.


class CustomerAdmin(admin.ModelAdmin):
    list_display = ('name', 'street', 'city', 'postal_code', 'technician',)


class ProfileAdmin(admin.ModelAdmin):
    fielist_displaylds = ('reference', 'name', 'rank',)


class PersonAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'phone', 'customer', 'profile',)


class TicketAdmin(admin.ModelAdmin):
    list_display = ('location', 'description',
                    'person', 'customer', 'technician',)


admin.site.register(Customer, CustomerAdmin)
admin.site.register(Profile, ProfileAdmin)
admin.site.register(Person, PersonAdmin)
admin.site.register(Ticket, TicketAdmin)
