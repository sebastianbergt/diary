# diary

```sql
CREATE USER diary WITH PASSWORD '1234';
CREATE DATABASE diary;
GRANT CONNECT ON DATABASE diary TO diary;
GRANT USAGE ON SCHEMA public TO diary;
ALTER DEFAULT PRIVILEGES IN SCHEMA public GRANT SELECT, INSERT, UPDATE, DELETE ON TABLES TO diary;
ALTER DEFAULT PRIVILEGES IN SCHEMA public GRANT USAGE, SELECT ON SEQUENCES TO diary;
```


```shell
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```