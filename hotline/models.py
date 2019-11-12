# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User, Group
from django.core.validators import RegexValidator

# Create your models here.


class Customer(models.Model):
    name = models.CharField(max_length=255, null=False,
                            default="New customer", unique=True)
    street = models.CharField(max_length=255, null=True)
    city = models.CharField(max_length=255, null=True)
    postal_code = models.CharField(
        max_length=5,
        validators=[
            RegexValidator(
                regex=r'^\d{5}$',
                message='Postal code must be entered in the format: \'99999\'.'
            )
        ],
        null=True
    )
    technician = models.ForeignKey(
        'Person', on_delete=models.PROTECT, related_name='+', null=True)

    def __str__(self):
        return self.name


class Profil(models.Model):
    reference = models.CharField(max_length=10)
    name = models.CharField(max_length=100)
    rank = models.IntegerField()

    def __str__(self):
        return self.name


class Person(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    phone = models.CharField(
        max_length=15,
        validators=[
            RegexValidator(
                regex=r'^\+?1?\d{9,15}$',
                message='Phone number must be entered in the format: \'+999999999\'. Up to 15 digits allowed.'
            )
        ],
        null=True
    )
    customer = models.ForeignKey(
        Customer, on_delete=models.PROTECT)
    profil = models.ForeignKey(
        Profil, on_delete=models.PROTECT)

    def __str__(self):
        return self.user.username


class Ticket(models.Model):
    location = models.CharField(max_length=255)
    description = models.TextField()
    person = models.ForeignKey(
        Person, related_name='tickets', on_delete=models.PROTECT, null=True)
    customer = models.ForeignKey(
        Customer, related_name='tickets', on_delete=models.PROTECT)
    technician = models.ForeignKey(
        Person, related_name='assigned_tickets', on_delete=models.PROTECT, null=True)

    def __str__(self):
        return self.location
