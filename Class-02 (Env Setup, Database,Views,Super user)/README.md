Database Migration
Migrations are Django’s way of propagating changes we make to our models (adding a field, deleting a model, etc.) into our database schema.

Make migrations:
  python manage.py makemigrations
Migrate:
  python manage.py migrate
Django framework have a build-in database named db.sqlite3. To manage our database we used DB SQLite3 Server. If it not availabe in our computer we need to download and install this.

Download Link:
[Download SQLiteBrowser 64-bit Windows](https://download.sqlitebrowser.org/DB.Browser.for.SQLite-3.12.2-win64.msi) <br>
[Download SQLiteBrowser 32-bit Windows](https://download.sqlitebrowser.org/DB.Browser.for.SQLite-3.12.2-win32.msi)

How to Create Super User
How to Display some text in web browser? Also add custom urls