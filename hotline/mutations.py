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

    def mutate_and_get_payload(self, info, **kwargs):
        technician_node, technician_id = from_global_id(
            kwargs.get('technician'))

        customer = Customer(
            name=kwargs.get('name'),
            street=kwargs.get('street'),
            city=kwargs.get('city'),
            postal_code=kwargs.get('postal_code'),
            technician=Person.objects.get(id=technician_id),
        )
        customer.save()
        return CreateCustomer(customer=customer)


class UpdateCustomer(graphene.relay.ClientIDMutation):
    customer = graphene.Field(CustomerNode)

    class Input:
        id = graphene.String()
        name = graphene.String(required=False)
        street = graphene.String(require=False)
        city = graphene.String(required=False)
        postal_code = graphene.String(required=False)
        technician = graphene.String(required=False)

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
            id=from_global_id(customer_id))
        customer.delete()
        return DeleteCustomer(customer=customer)


class CreateProfil(graphene.relay.ClientIDMutation):
    profil = graphene.Field(ProfilNode)

    class Input:
        reference = graphene.String()
        name = graphene.String()
        rank = graphene.Int()

    def mutate_and_get_payload(self, info, **kwargs):
        profil = Profil(
            name=kwargs.get('name'),
            reference=kwargs.get('reference'),
            rank=kwargs.get('rank'),
        )
        profil.save()
        return CreateProfil(profil=profil)


class UpdateProfil(graphene.relay.ClientIDMutation):
    profil = graphene.Field(ProfilNode)

    class Input:
        id = graphene.String()
        reference = graphene.String(required=False)
        name = graphene.String(required=False, null=True)
        rank = graphene.Int(required=False)

    def mutate_and_get_payload(self, info, **kwargs):
        profil_node, profil_id = from_global_id(
            kwargs.get('id'))

        profil = Profil.objects.get(id=profil_id)
        if 'reference' in kwargs:
            profil.reference = kwargs.get('reference')
        if 'name' in kwargs:
            profil.name = kwargs.get('name')
        if 'rank' in kwargs:
            profil.rank = kwargs.get('rank')
        profil.save()
        return UpdateProfil(profil=profil)


class CreatePerson(graphene.relay.ClientIDMutation):
    person = graphene.Field(PersonNode)

    class Input:
        user = graphene.String()
        phone = graphene.String()
        customer = graphene.String()
        profil = graphene.String()

    def mutate_and_get_payload(self, info, **kwargs):
        user_node, user_id = from_global_id(kwargs.get('user'))
        customer_node, customer_id = from_global_id(kwargs.get('customer'))
        profil_node, profil_id = from_global_id(kwargs.get('profil'))

        person = Profil(
            user=User.objects.get(id=user_id),
            phone=kwargs.get('reference'),
            customer=Customer.objects.get(id=customer_id),
            profil=Profil.objects.get(id=profil_id),
        )
        person.save()
        return CreatePerson(person=person)


class UpdatePerson(graphene.relay.ClientIDMutation):
    person = graphene.Field(PersonNode)

    class Input:
        id = graphene.String()
        user = graphene.String(required=False)
        phone = graphene.String(required=False, null=True)
        customer = graphene.String(required=False)
        profil = graphene.String(required=False)

    def mutate_and_get_payload(self, info, **kwargs):
        person_node, person_id = from_global_id(
            kwargs.get('id'))
        print('----------')
        print(kwargs)
        print('----------')

        person = Person.objects.get(id=person_id)
        if 'user' in kwargs:
            user_node, user_id = from_global_id(
                kwargs.get('user'))
            person.user = User.objects.get(id=user_id)
        if 'phone' in kwargs:
            person.phone = kwargs.get('phone')
        if 'customer' in kwargs:
            customer_node, customer_id = from_global_id(
                kwargs.get('customer'))
            person.customer = Customer.objects.get(id=customer_id)
        if 'profil' in kwargs:
            profil_node, profil_id = from_global_id(
                kwargs.get('profil'))
            person.profil = Profil.objects.get(id=profil_id)
        person.save()
        return UpdatePerson(person=person)


class CreateTicket(graphene.relay.ClientIDMutation):
    ticket = graphene.Field(PersonNode)

    class Input:
        location = graphene.String()
        description = graphene.String()
        person = graphene.String()
        customer = graphene.String()
        technician = graphene.String()

    def mutate_and_get_payload(self, info, **kwargs):
        person_node, person_id = from_global_id(kwargs.get('person'))
        customer_node, customer_id = from_global_id(kwargs.get('customer'))
        technician_node, technician_id = from_global_id(
            kwargs.get('technician'))

        ticket = Profil(
            location=kwargs.get('location'),
            description=kwargs.get('description'),
            person=Person.objects.get(id=person_id),
            customer=Customer.objects.get(id=customer_id),
            technician=Person.objects.get(id=technician_id),
        )
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
        ticket.save()
        return UpdateTicket(ticket=ticket)
