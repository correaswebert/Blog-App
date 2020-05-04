- Project is divided into multiple apps, each with its own usecase.
  So our main project can be divided into multiple apps like a blog
  app, store app, etc.

- When we search for url from our main project, it tries to match it
  in the order of the _urlpatterns_ list
  If a match is found, then site is redirected to that app and the
  matched portion of the url is trimmed before the app tries to do
  the same with its _urlpatterns_ to redirect to the views (webpage).

- When using templates, add the name of the _AppConfig_ (in the
  app directory's **apps.py**) to the _INSTALLED_APPS_ list
  in **settings.py** of the project

- Views must return an _HttpResponse_ or exception...
  _render_ function returns it behind the scenes

- URL redirects from pages should be aliased using the names defined
  in the **urls.py** of the app, instead of hardcoding the path
  This way, it is easy to change routes (or existing path names)

- All static content should be placed in the
  **static** folder...

- `python3 manage.py sqlmigrate _appname_ _migrationNumber_`
  this command will print out the SQL query done when our **models.py**
  file creates a ORM (_makemigrations_ command is rum)

- Migrations does the SQL query changes under the hood, so we do not
  have to worry about it... even when database is populated

- `python manage.py shell`
  this command gives Django based python interactive shell
