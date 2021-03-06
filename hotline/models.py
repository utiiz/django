# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User, Group
from django.core.validators import RegexValidator
from django.contrib.postgres.fields import ArrayField

# Create your models here.


class Customer(models.Model):
    name = models.CharField(max_length=255, null=False, unique=True)
    street = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=255, blank=True, null=True)
    postal_code = models.CharField(
        max_length=5,
        validators=[
            RegexValidator(
                regex=r'^\d{5}$',
                message='Postal code must be entered in the format: \'99999\'.'
            )
        ],
        blank=True,
        null=True
    )
    technician = models.ForeignKey(
        'Person', on_delete=models.PROTECT, related_name='+', blank=True, null=True)
    persons = models.ManyToManyField('Person', related_name='customers')

    def __str__(self):
        return self.name


class Profile(models.Model):
    reference = models.CharField(max_length=10, null=False, unique=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    rank = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.name


class Person(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.PROTECT, blank=True, null=True)
    phone = models.CharField(
        max_length=15,
        validators=[
            RegexValidator(
                regex=r'^\+?1?\d{9,15}$',
                message='Phone number must be entered in the format: \'+999999999\'. Up to 15 digits allowed.'
            )
        ],
        blank=True,
        null=True
    )
    # customers = models.ManyToManyField(Customer, related_name='persons')
    profile = models.ForeignKey(
        Profile, related_name="persons", on_delete=models.PROTECT,
        blank=True,
        null=True)

    def __str__(self):
        return self.user.username


class Parameter(models.Model):
    reference = models.CharField(max_length=15, blank=True, null=True)
    name = models.CharField(max_length=50, blank=True, null=True)
    type = models.CharField(max_length=15, blank=True, null=True)
    rank = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.user.username


class Ticket(models.Model):
    location = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    person = models.ForeignKey(
        Person, related_name='tickets', on_delete=models.PROTECT, blank=True, null=True)
    customer = models.ForeignKey(
        Customer, related_name='tickets', on_delete=models.PROTECT, blank=True, null=True)
    technician = models.ForeignKey(
        Person, related_name='assigned_tickets', on_delete=models.PROTECT, blank=True, null=True)
    attachments = ArrayField(models.CharField(max_length=1024), blank=True, null=True)

    def __str__(self):
        return self.location
