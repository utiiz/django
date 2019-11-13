import graphene
from graphql_relay.node.node import from_global_id
from .models import *
from .nodes import *


class CreateCustomer(graphene.relay.ClientIDMutation):
    customer = graphene.Field(CustomerNode)

    class Input:
        name = graphene.String()
        street = graphene.String()
        city = graphene.String()
        postal_code = graphene.String()
        technician = graphene.String()
        persons = graphene.List(graphene.String)

    def mutate_and_get_payload(self, info, **kwargs):

        customer = Customer()

        if 'name' in kwargs:
            customer.name = kwargs.get('name')
        if 'street' in kwargs:
            customer.street = kwargs.get('street')
        if 'city' in kwargs:
            customer.city = kwargs.get('city')
        if 'postal_code' in kwargs:
            customer.postal_code = kwargs.get('postal_code')
        if 'technician' in kwargs:
            technician_node, technician_id = from_global_id(
                kwargs.get('technician'))
            customer.technician = Person.objects.get(id=technician_id)
        customer.save()
        if 'persons' in kwargs:
            for item in kwargs.get('persons'):
                person_node, person_id = from_global_id(item)
                p = Person.objects.get(id=person_id)
                customer.persons.add(p)
        return CreateCustomer(customer=customer)


class UpdateCustomer(graphene.relay.ClientIDMutation):
    customer = graphene.Field(CustomerNode)

    class Input:
        id = graphene.String()
        name = graphene.String(required=False, default_value=None)
        street = graphene.String(
            require=False, blank=True, null=True, default_value=None)
        city = graphene.String(required=False, default_value=None)
        postal_code = graphene.String(required=False, default_value=None)
        technician = graphene.String(required=False, default_value=None)
        persons = graphene.List(graphene.String)
        removed_persons = graphene.List(graphene.String)
        null = graphene.List(graphene.String)

    def mutate_and_get_payload(self, info, **kwargs):
        customer_node, customer_id = from_global_id(
            kwargs.get('id'))

        customer = Customer.objects.get(id=customer_id)
        if 'name' in kwargs:
            customer.name = kwargs.get('name')
        if 'street' in kwargs:
            customer.street = kwargs.get('street')
        if 'city' in kwargs:
            customer.city = kwargs.get('city')
        if 'postal_code' in kwargs:
            customer.postal_code = kwargs.get('postal_code')
        if 'technician' in kwargs:
            technician_node, technician_id = from_global_id(
                kwargs.get('technician'))
            customer.technician = Person.objects.get(id=technician_id)

        if 'persons' in kwargs:
            customer.persons.clear()
            for item in kwargs.get('persons'):
                person_node, person_id = from_global_id(item)
                p = Person.objects.get(id=person_id)
                customer.persons.add(p)

        '''
        if 'removed_persons' in kwargs:
            for item in kwargs.get('removed_persons'):
                person_node, person_id = from_global_id(item)
                p = Person.objects.get(id=person_id)
                customer.persons.remove(p)
        '''

        if 'null' in kwargs:
            for item in kwargs.get('null'):
                setattr(customer, item, None)

        customer.save()
        return UpdateCustomer(customer=customer)


class DeleteCustomer(graphene.relay.ClientIDMutation):
    customer = graphene.Field(CustomerNode)

    class Input:
        id = graphene.String()

    def mutate_and_get_payload(self, info, **kwargs):
        customer_node, customer_id = from_global_id(
            kwargs.get('id'))
        customer = Customer.objects.get(
            id=customer_id)
        customer.delete()
        return DeleteCustomer(customer=customer)


class CreateProfile(graphene.relay.ClientIDMutation):
    profile = graphene.Field(ProfileNode)

    class Input:
        reference = graphene.String()
        name = graphene.String()
        rank = graphene.Int()

    def mutate_and_get_payload(self, info, **kwargs):
        profile = Profile()
        if 'reference' in kwargs:
            profile.reference = kwargs.get('reference')
        if 'name' in kwargs:
            profile.name = kwargs.get('name')
        if 'rank' in kwargs:
            profile.rank = kwargs.get('rank')
        profile.save()
        return CreateProfile(profile=profile)


class UpdateProfile(graphene.relay.ClientIDMutation):
    profile = graphene.Field(ProfileNode)

    class Input:
        id = graphene.String()
        reference = graphene.String(required=False)
        name = graphene.String(required=False, null=True)
        rank = graphene.Int(required=False)
        null = graphene.List(graphene.String)

    def mutate_and_get_payload(self, info, **kwargs):
        profile_node, profile_id = from_global_id(
            kwargs.get('id'))

        profile = Profile.objects.get(id=profile_id)
        if 'reference' in kwargs:
            profile.reference = kwargs.get('reference')
        if 'name' in kwargs:
            profile.name = kwargs.get('name')
        if 'rank' in kwargs:
            profile.rank = kwargs.get('rank')

        if 'null' in kwargs:
            for item in kwargs.get('null'):
                setattr(profile, item, None)

        profile.save()
        return UpdateProfile(profile=profile)


class DeleteProfile(graphene.relay.ClientIDMutation):
    profile = graphene.Field(ProfileNode)

    class Input:
        id = graphene.String()

    def mutate_and_get_payload(self, info, **kwargs):
        profile_node, profile_id = from_global_id(
            kwargs.get('id'))
        profile = Profile.objects.get(
            id=profile_id)
        profile.delete()
        return DeleteProfile(profile=profile)


class CreatePerson(graphene.relay.ClientIDMutation):
    person = graphene.Field(PersonNode)

    class Input:
        user = graphene.String()
        phone = graphene.String()
        customers = graphene.List(graphene.String)
        profile = graphene.String()

    def mutate_and_get_payload(self, info, **kwargs):

        person = Profile()
        if 'user' in kwargs:
            user_node, user_id = from_global_id(
                kwargs.get('user'))
            person.user = User.objects.get(id=user_id)
        if 'phone' in kwargs:
            person.phone = kwargs.get('phone')
        if 'profile' in kwargs:
            profile_node, profile_id = from_global_id(
                kwargs.get('profile'))
            person.profile = Profile.objects.get(id=profile_id)
        person.save()

        
        if 'customers' in kwargs:
            for customer in kwargs.get('customers'):
                customer_node, customer_id = from_global_id(customer)
                c = Customer.objects.get(id=customer_id)
                person.customers.add(c)

        return CreatePerson(person=person)


class UpdatePerson(graphene.relay.ClientIDMutation):
    person = graphene.Field(PersonNode)

    class Input:
        id = graphene.String()
        user = graphene.String(required=False)
        phone = graphene.String(required=False, null=True)
        customers = graphene.List(graphene.String)
        profile = graphene.String(required=False)
        null = graphene.List(graphene.String)

    def mutate_and_get_payload(self, info, **kwargs):
        person_node, person_id = from_global_id(
            kwargs.get('id'))

        person = Person.objects.get(id=person_id)
        if 'user' in kwargs:
            user_node, user_id = from_global_id(
                kwargs.get('user'))
            person.user = User.objects.get(id=user_id)
        if 'phone' in kwargs:
            person.phone = kwargs.get('phone')
        if 'customers' in kwargs:
            person.customers.clear()
            for item in kwargs.get('persons'):
                customer_node, customer_id = from_global_id(item)
                c = Customer.objects.get(id=customer_id)
                person.customers.add(c)
        if 'profile' in kwargs:
            profile_node, profile_id = from_global_id(
                kwargs.get('profile'))
            person.profile = Profile.objects.get(id=profile_id)

        

        if 'null' in kwargs:
            for item in kwargs.get('null'):
                setattr(person, item, None)

        person.save()
        return UpdatePerson(person=person)


class DeletePerson(graphene.relay.ClientIDMutation):
    person = graphene.Field(PersonNode)

    class Input:
        id = graphene.String()

    def mutate_and_get_payload(self, info, **kwargs):
        person_node, person_id = from_global_id(
            kwargs.get('id'))
        person = Person.objects.get(
            id=person_id)
        person.delete()
        return DeletePerson(person=person)


class CreateTicket(graphene.relay.ClientIDMutation):
    ticket = graphene.Field(PersonNode)

    class Input:
        location = graphene.String()
        description = graphene.String()
        person = graphene.String()
        customer = graphene.String()
        technician = graphene.String()

    def mutate_and_get_payload(self, info, **kwargs):

        ticket = Profile()
        if 'location' in kwargs:
            ticket.location = kwargs.get('location')
        if 'description' in kwargs:
            ticket.description = kwargs.get('description')
        if 'person' in kwargs:
            person_node, person_id = from_global_id(
                kwargs.get('person'))
            ticket.person = Person.objects.get(id=person_id)
        if 'customer' in kwargs:
            customer_node, customer_id = from_global_id(
                kwargs.get('customer'))
            ticket.customer = Customer.objects.get(id=customer_id)
        if 'technician' in kwargs:
            technician_node, technician_id = from_global_id(
                kwargs.get('technician'))
            ticket.technician = Person.objects.get(id=technician_id)
        ticket.save()
        return CreateTicket(ticket=ticket)


class UpdateTicket(graphene.relay.ClientIDMutation):
    ticket = graphene.Field(TicketNode)

    class Input:
        id = graphene.String()
        location = graphene.String(required=False)
        description = graphene.String(required=False)
        person = graphene.String(required=False)
        customer = graphene.String(required=False)
        technician = graphene.String(required=False)
        null = graphene.List(graphene.String)

    def mutate_and_get_payload(self, info, **kwargs):
        ticket_node, ticket_id = from_global_id(
            kwargs.get('id'))

        ticket = Ticket.objects.get(id=ticket_id)

        if 'location' in kwargs:
            ticket.location = kwargs.get('location')
        if 'description' in kwargs:
            ticket.description = kwargs.get('description')
        if 'person' in kwargs:
            person_node, person_id = from_global_id(
                kwargs.get('person'))
            ticket.person = Person.objects.get(id=person_id)
        if 'customer' in kwargs:
            customer_node, customer_id = from_global_id(
                kwargs.get('customer'))
            ticket.customer = Customer.objects.get(id=customer_id)
        if 'technician' in kwargs:
            technician_node, technician_id = from_global_id(
                kwargs.get('technician'))
            ticket.technician = Person.objects.get(id=technician_id)

        if 'null' in kwargs:
            for item in kwargs.get('null'):
                setattr(ticket, item, None)

        ticket.save()
        return UpdateTicket(ticket=ticket)


class DeleteTicket(graphene.relay.ClientIDMutation):
    ticket = graphene.Field(TicketNode)

    class Input:
        id = graphene.String()

    def mutate_and_get_payload(self, info, **kwargs):
        ticket_node, ticket_id = from_global_id(
            kwargs.get('id'))
        ticket = Ticket.objects.get(
            id=ticket_id)
        ticket.delete()
        return DeleteTicket(ticket=ticket)
