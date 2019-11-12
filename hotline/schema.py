import graphene
from graphene_django.types import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField
from graphql_relay.node.node import from_global_id
from .models import *
from .nodes import *
from .mutations import *


class Query(graphene.ObjectType):
    customer = graphene.relay.Node.Field(CustomerNode)
    customers = DjangoFilterConnectionField(CustomerNode)

    profile = graphene.relay.Node.Field(ProfileNode)
    profiles = DjangoFilterConnectionField(ProfileNode)

    person = graphene.relay.Node.Field(PersonNode)
    persons = DjangoFilterConnectionField(PersonNode)

    ticket = graphene.relay.Node.Field(TicketNode)
    tickets = DjangoFilterConnectionField(TicketNode)

    user = graphene.relay.Node.Field(UserNode)
    users = DjangoFilterConnectionField(UserNode)


# MUTATIONS
class Mutation(graphene.AbstractType):
    create_customer = CreateCustomer.Field()
    create_profile = CreateProfile.Field()
    create_person = CreatePerson.Field()
    create_ticket = CreateTicket.Field()

    update_customer = UpdateCustomer.Field()
    update_profile = UpdateProfile.Field()
    update_person = UpdatePerson.Field()
    update_ticket = UpdateTicket.Field()

    delete_customer = DeleteCustomer.Field()
    delete_profile = DeleteProfile.Field()
    delete_person = DeletePerson.Field()
    delete_ticket = DeleteTicket.Field()
