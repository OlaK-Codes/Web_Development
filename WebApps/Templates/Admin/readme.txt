Create Folder: Admin
|
Create Project : admin_sys
|
Creatr and Activate Environment:
cd Admin
source p_env/bin/activate
|
Create new app:
django-admin startapp crm
|
add in settings new app crm
|
Check server: python manage.py runserver 
|
Migrate default db migration:
python manage.py migrate
|
Access to default admin panel:
python manage.py runserver 
http://127.0.0.1:8000/admin/login/?next=/admin/
|
create admin user:
python manage.py createsuperuser
o.k.
ola.k.contact@gmail.com
ghj567
|
create own data models in models.py (tables for db)
|
modify default db model :
python manage.py makemigrations
|
Confirm changed db model
python manage.py migrate
|
Import this model in admin dashboard (3 methods)
go admin.py write code
python manage.py runserver 


