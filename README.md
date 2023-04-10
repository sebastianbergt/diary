# diary

Allows each user to create one private diary entry a day.

## SQL setup

```sql
CREATE USER diary WITH PASSWORD '1234';
CREATE DATABASE diary;
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
