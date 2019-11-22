# Postgres
[Postgres Install](https://www.digitalocean.com/community/tutorials/how-to-install-and-use-postgresql-on-ubuntu-18-04)
```zsh
sudo apt-get install postgresql
sudo -u postgres createuser --interactive
psql
```

# Python

```zsh
pip install pipenv
pipenv shell
# pipenv shell --python /usr/local/bin/python3.8
pip install django
pip install graphene_django
# sudo apt-get install python-psycopg2
# sudo apt-get install libpq-dev
pip install psycopg2
pip install django-filter

py manage.py migrate
# If it doesn't work change the /etc/postgresql/9.8/main/pg_hba.conf peer -> md5
# Then sudo /etc/init.d/postgresql reload
# Then sudo service postgresql restart

py manage.py createsuperuser

py manage.py runserver
```