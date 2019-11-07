import graphene
from graphene_django import DjangoObjectType
from .models import *
from graphene_django.filter import DjangoFilterConnectionField


class CustomerNode(DjangoObjectType):
    class Meta:
        model = Customer
        filter_fields = ['name', 'street', 'city', 'postal_code', ]
        interfaces = (graphene.relay.Node,)


class ProfilNode(DjangoObjectType):
    class Meta:
        model = Profil
        filter_fields = ['reference', 'name', 'rank', ]
        interfaces = (graphene.relay.Node,)


class PersonNode(DjangoObjectType):
    class Meta:
        model = Person
        filter_fields = ['user', 'phone', 'customer', 'profil', ]
        interfaces = (graphene.relay.Node,)


class TicketNode(DjangoObjectType):
    class Meta:
        model = Ticket
        filter_fields = ['location', 'description',
                         'user', 'customer', 'technician', ]
        interfaces = (graphene.relay.Node,)


class Query(object):
    customer = graphene.relay.Node.Field(CustomerNode)
    customers = DjangoFilterConnectionField(CustomerNode)

    profil = graphene.relay.Node.Field(ProfilNode)
    profils = DjangoFilterConnectionField(ProfilNode)

    person = graphene.relay.Node.Field(PersonNode)
    persons = DjangoFilterConnectionField(PersonNode)

    ticket = graphene.relay.Node.Field(TicketNode)
    tickets = DjangoFilterConnectionField(TicketNode)
