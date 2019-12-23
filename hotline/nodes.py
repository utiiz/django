import graphene
from graphene_django.types import DjangoObjectType
from .models import *


class CustomerNode(DjangoObjectType):
    class Meta:
        model = Customer
        filter_fields = ['name', 'street',
                         'city', 'postal_code', 'technician', ]
        interfaces = (graphene.relay.Node,)


class ProfileNode(DjangoObjectType):
    class Meta:
        model = Profile
        filter_fields = ['reference', 'name', 'rank', ]
        interfaces = (graphene.relay.Node,)


class PersonNode(DjangoObjectType):
    class Meta:
        model = Person
        filter_fields = ['user', 'phone', 'profile', ]
        interfaces = (graphene.relay.Node,)


class ParameterNode(DjangoObjectType):
    class Meta:
        model = Parameter
        filter_fields = ['reference', 'name', 'type', 'rank', ]
        interfaces = (graphene.relay.Node,)


class TicketNode(DjangoObjectType):
    class Meta:
        model = Ticket
        # filter_fields = ['location', 'description',
        #                  'person', 'customer', 'technician', ]
        filter_fields = {
            'location': ['exact', 'icontains', 'istartswith'],
            'description': ['exact', 'icontains', 'istartswith'],
            'person': ['exact'],
            'customer': ['exact'],
            'technician': ['exact'],
        }
        interfaces = (graphene.relay.Node,)


class UserNode(DjangoObjectType):
    class Meta:
        model = User
        filter_fields = ['username', 'first_name', 'last_name', 'email']
        interfaces = (graphene.relay.Node,)
