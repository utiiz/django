import graphene
from graphene_django.filter import DjangoFilterConnectionField
from graphene_django.types import DjangoObjectType
from .models import *


class CustomerNode(DjangoObjectType):
    class Meta:
        model = Customer
        interfaces = (graphene.relay.Node,)
        filter_fields = ['name', 'street', 'city', 'postal_code', ]


class ProfilNode(DjangoObjectType):
    class Meta:
        model = Profil
        interfaces = (graphene.relay.Node,)
        filter_fields = ['reference', 'name', 'rank', ]


class PersonNode(DjangoObjectType):
    class Meta:
        model = Person
        interfaces = (graphene.relay.Node,)
        filter_fields = ['user', 'phone', 'customer', 'profil', ]


class TicketNode(DjangoObjectType):
    class Meta:
        model = Ticket
        interfaces = (graphene.relay.Node,)
        filter_fields = ['location', 'description',
                         'user', 'customer', 'technician', ]


class Query(graphene.ObjectType):
    customer = graphene.relay.Node.Field(CustomerNode)
    customers = DjangoFilterConnectionField(CustomerNode)

    profil = graphene.relay.Node.Field(ProfilNode)
    profils = DjangoFilterConnectionField(ProfilNode)

    person = graphene.relay.Node.Field(PersonNode)
    persons = DjangoFilterConnectionField(PersonNode)

    ticket = graphene.relay.Node.Field(TicketNode)
    tickets = DjangoFilterConnectionField(TicketNode)
