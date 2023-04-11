# diary

Allows each user to create one private diary entry a day.

## SQL setup


Edit the template1 to allow utf8
```sql
UPDATE pg_database SET datistemplate = FALSE WHERE datname = 'template1';
DROP DATABASE template1;
CREATE DATABASE template1 WITH TEMPLATE = template0 ENCODING = 'UTF8';
UPDATE pg_database SET datistemplate = TRUE WHERE datname = 'template1';
\c template1;
VACUUM FREEZE;
```

Create user and database, and grant access
```sql
CREATE USER diary WITH PASSWORD '1234';
CREATE DATABASE diary ENCODING 'UTF8';

GRANT CONNECT ON DATABASE diary TO diary;
GRANT USAGE ON SCHEMA public TO diary;
ALTER DEFAULT PRIVILEGES IN SCHEMA public GRANT SELECT, INSERT, UPDATE, DELETE ON TABLES TO diary;
ALTER DEFAULT PRIVILEGES IN SCHEMA public GRANT USAGE, SELECT ON SEQUENCES TO diary;
```

## Getting migrations in line

```shell
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

## Key renewal

```shell
cd ansible-files
openssl req -x509 -newkey rsa:4096 -sha256 -days 3650 -nodes \
  -keyout nginx_https.key -out nginx_https.crt -subj "/CN=192.168.1.150" \
  -addext "subjectAltName=DNS:192.168.1.150,DNS:192.168.1.150,IP:192.168.1.150"
```

## Deployment

```shell
ansible-playbook -i inventory.yml playbook-deploy-django.yml
```
