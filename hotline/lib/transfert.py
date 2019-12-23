import json

output = []

_users = []
_profiles = []
_persons = []
_customers = []
_parameters = []
_tickets = []

def write(data) :
    with open('data.json', 'w') as outfile:
        json.dump(data, outfile)

def dataFilter(datas, name):
    for data in datas:
        if data['type'] == 'table' and data['name'] == name:
            return data['data']
    return None

def profileFilter(profiles, reference):
    for profile in profiles:
        if profile['fields']['reference'] == reference:
            return profile
    return None

def personFilter(persons, old_pk):
    for person in persons:
        if person['old_pk'] == int(old_pk):
            return person
    return None

def customerFilter(customers, old_pk):
    for customer in customers:
        if customer['old_pk'] == int(old_pk):
            return customer
    return None

def ticketFilter(tickets, old_pk):
    for ticket in tickets:
        if ticket['old_pk'] == int(old_pk):
            return ticket
    return None

def getUsername(users, username) :
    for user in users:
        if user['fields']['username'] == username:
            try:
                username = username[:-1] + str(int(username[-1:]) + 1)
                print(username, username[-1:], int(username[-1:]))
            except ValueError:
                username = username + "1"
                pass
    return username

with open('./datas.json') as f:
    datas = json.load(f)
    profiles = dataFilter(datas, 'profil')
    for i in range(len(profiles)):
        _profiles.append({
            "model": "hotline.profile",
            "pk": i + 1,
            "fields": {
                "reference": profiles[i]['refProfil'],
                "name": profiles[i]['libelle'],
                "rank": int(profiles[i]['rang'])
            }
        })

    users = dataFilter(datas, 'utilisateur')
    for i in range(len(users)):
        u = users[i]
        username = getUsername(_users, u['login'])
        _users.append({
            "model": "auth.user",
            "old_pk": int(u['idUtilisateur']),
            "pk": i + 1,
            "fields": {
                "password": "pbkdf2_sha256$150000$fgGbJ131MFdU$OUewF371fZxbH6E94NodAzMaAXAmoTdZ6WBirG52XL8=",
                "is_superuser": False,
                "username": username,
                "first_name": u['prenom'].title(),
                "last_name": u['nom'].title(),
                "email": u['mail'],
                "is_staff": False,
                "is_active": True
            }
        })

        profile = profileFilter(_profiles, u['refProfil'])
        _persons.append({
            "model": "hotline.person",
            "old_pk": int(u['idUtilisateur']),
            "pk": i + 1,
            "fields": {
                "user": i + 1,
                "phone": None if u['tel'] == '' else u['tel'],
                "profile": profile['pk']
            }
        })
        
    customers = dataFilter(datas, 'client')
    for i in range(len(customers)):
        c = customers[i]

        person = personFilter(_persons, c['idTechnicien'])

        _customers.append({
            "model": "hotline.customer",
            "old_pk": int(c['idClient']),
            "pk": i + 1,
            "fields": {
                "name": c['nom'].title(),
                "street": c['adresseRue'].title(),
                "city": c['adresseVille'].title(),
                "postal_code": c['cp'],
                "technician": person['pk'],
                "persons": []
            }
        })
    
    relations = dataFilter(datas, 'relation')
    for i in range(len(relations)):
        r = relations[i]

        customer = customerFilter(_customers, r['idClient'])
        person = personFilter(_persons, r['idUtilisateur'])

        if customer and person:
            if not person['pk'] in customer['fields']['persons']:
                customer['fields']['persons'].append(person['pk'])
            
    parameters = dataFilter(datas, 'parametre')
    for i in range(len(parameters)):
        p = parameters[i]

        _parameters.append({
                "model": "hotline.parameter",
                "old_pk": p['refParametre'],
                "pk": i + 1,
                "fields": {
                    "reference": p['refParametre'],
                    "name": p['libelle'],
                    "type": p['type'],
                    "rank": p['rang']
                }
            })

    tickets = dataFilter(datas, 'ticket')
    for i in range(len(tickets)):
        t = tickets[i]

        person = personFilter(_persons, t['idUtilisateur'])
        technician = personFilter(_persons, t['idTechnicien'])
        customer = customerFilter(_customers, t['idClient'])

        if person and technician and customer:
            _tickets.append({
                "model": "hotline.ticket",
                "old_pk": int(t['idTicket']),
                "pk": i + 1,
                "fields": {
                    "location": t['localisation'],
                    "description": t['description'],
                    "person": person['pk'],
                    "customer": customer['pk'],
                    "technician": technician['pk'],
                    "attachments": []
                }
            })

    attachments = dataFilter(datas, 'piece_jointe')
    for i in range(len(attachments)):
        a = attachments[i]

        ticket = ticketFilter(_tickets, a['idTicket'])

        if ticket:
            ticket['fields']['attachments'].append(a['chemin'])

    output = _users + _profiles + _persons + _customers + _parameters + _tickets

    for o in output:
        if 'old_pk' in o:
            del o['old_pk']

    write(output)