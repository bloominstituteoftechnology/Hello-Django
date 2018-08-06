 Day 1
-------------------------------------
# Summary
* Get pipenv installed
* Clone your repo
  * (If you cloned the Hello-Django repo, delete the file requirements.txt!)
* Go to your repo root directory
* pipenv --three
* pipenv install django
* pipenv shell
* django-admin startproject djorg .
* django-admin startapp notes
* ./manage.py runserver
* ./manage.py showmigrations
* ./manage.py migrate
* ./manage.py runserver
* Add model to notes/models.py
* Add 'notes' to INSTALLED_APPS in djorg/settings.py
* ./manage.py showmigrations
* ./manage.py makemigrations
* ./manage.py showmigrations
* ./manage.py migrate
* ./manage.py shell
  * from notes.models import Note
  * n = Note(title=”example”, content=”This is a test.”)
  * n.save()
  * exit()
* ./manage.py shell
  * from notes.models import Note
  * x = Note.objects.all()
  * x[0]
  * x[0].content
  * exit()
* pipenv install python-decouple
* Add config information to settings.py and .env

# To Start a Django Project and App:

## Check Python version and install or upgrade if less than 3.5.x
## Check Pip version and install or upgrade if less than 10.x

* Mac/Linux - Option A: `sudo -H pip3 install --upgrade pip`
* Mac/Linux - Option B: `brew upgrade python`
* PC - `python -m pip install --upgrade pip`

## Check Pipenv version and install or upgrade if less than 2018.x

Create a repo in github
* With README
* With Python .gitignore

Clone repo on to local machine

In the terminal, navigate to root folder of repo

Create pipenv virtual environment with `pipenv --three`
* The --three option tells it to use Python3
* This is similar to using npm/yarn

Verify that the Pipfile was created in the root of the repo

Activate pipenv with `pipenv shell`
* You should see the command line change to the name of your repo/folder followed by a dash and a random string
* We are using pipenv because it is newer and more robust.  Uses a lockfile similar to npm/yarn.  Easier to get into and out of shell
* To get back in, use `pipenv shell` from the root directory of the project

Once you are in the virtual environment, install django with `pipenv install django`
* We are using a virtual environment instead of installing globally because installing globally would be like using npm/yarn install globally and installing all the packages on everything

Add pipfile and pipfile.lock to the repo with `git add Pipfile*` and commit with `git commit -m “added pipfiles”`

Start a project with `django-admin startproject [name_of_project] .`
* Replace [nameofproject] with the name of your project
* The . tells it to create the project in the current directory.  Otherwise, it would create a project in a subdirectory called [name_of_project].  We don’t need that because we want the repo folder to be the root

Verify that the [name_of_project] folder was created and has boilerplate files such as __init__.py
The project is what it was named above.  A project is made up of a collection of apps.  It can have many.  

Create an app with `django-admin startapp [name_of_app]`
* For the first project, we are naming the app notes
* Name it differently as appropriate if you are following this to set up, but working on something else.

Verify that the [name_of_app] subdirectory has been created

Test by navigating to the project folder root/[name_of_project] and running `python manage.py runserver`
* This should launch the animated rocket default page
* Take note of the warning about unapplied migrations.  We will fix that in a moment

Django makes it easier to make changes to databases.  This is called migration(s)

Run `python manage.py showmigrations`.  This will show a list of outstanding changes that need to occur

To take a closer look at what is being done, run `python manage.py sqlmigrate [package_name] [migration_id], for example, `python manage.py sqlmigrate admin 0001_initial`
* This will display a large number of sql commands that may not make sense if you are not yet familiar with sql
* This doesn’t actually do anything.  It just displays info
* These are all the data structures that your python code has created.  Django turns this into sql tables, etc. for you.  (If you’ve ever done this manually, you know how awesome that is :) )

To actually run the migrations, use `python manage.py migrate`

Check them by showing migrations again - `python manage.py showmigrations`
* The list of migrations should show an `x` for each item

Run the server again and confirm that the migration warning is not present.  There won’t be a change to the actual page that renders

------------------------------
# Adding data and doing setup for the notes app:

In the `notes` folder, open `models.py`

Create a class called `notes` that inherits from `models.Model` - `class Note(models.Model):`

This gives our new class access to all of the built-in functionality in `models.Model`

Think about the data that we need for standard web notes functionality.  We might want a title, body, some timestamps, etc.  We can use the docs to find the types of things we can add:

https://docs.djangoproject.com/en/2.0/ref/models/

Add the following variables:

```
title = models.CharField(max_length=200)
content = models.TextField(blank=True)
created_at = models.DateTimeField(auto_now_add=True)
last_modified = models.DateTimeField(auto_now=True)
```
Add any additional fields you would like as well.

We also need something to serve as a unique identifier for each record.  We’ll use something called a UUID for this:  https://en.wikipedia.org/wiki/Universally_unique_identifier

Add a uuid to serve as a key for each record.  
* First, import the library - `from uuid import uuid4`
* Second, add the field - `id = models.UUIDField(primary_key=True, default=uuid4, editable=False)`
  * Primary key is how the database tracks records
  * Default calls a function to randomly generate a unique identifier
  * We make editable false because we never want to change the key
  * Put it at the top of the list of fields because it’s sort of like the index for the record

----------------------------
Next, we need to tell the project that the app exists.  Open `settings.py` from the project folder.

Find the section for `INSTALLED_APPS` and add `’notes’`, or other apps as appropriate.

In the console, check for migrations again with `python manage.py showmigrations`.  The notes app should show up in the list now, but it has no migrations.  

Run `python manage.py makemigrations` to generate them.  If you get an error that there are no changes to make, double-check that you have saved `models.py`.

Show migrations again to make sure they appear, then do the migration - `python manage.py migrate`

Manage.py has its own shell.  Run `python manage.py shell` to bring up a Python repl.  
* The input line should change to `>>>`

Import the notes class into the repl - `from notes.models import Note`

Create a new note with `n = Note(title=”example”, content=”This is a test.”)`

Check by the name of your variable to make sure worked - n
We can use a built in function from models to save this to the database - `n.save()`

Exit the terminal, then restart it - `exit()` then `python manage.py shell`

We have to import the `Note` class again, using the same command as before

There is another built in method that will retrieve all existing objects of a class - `Note.objects.all()`

Use this to save the data back into a variable named `b` and explore.

----------------------

Take a look at that secret key in `settings.py`

We want to move this out of the settings file so that it doesn’t get checked into source control.  We’ll move it to another file, which everyone on the project will need a copy of, but it won’t be in the repo itself.

We’re going to make use of a module called Python Decouple by installing it in the virtual environment = `pipenv install python-decouple`

Once it’s installed, we can bring it into `settings.py` with `from decouple import config`

Pull up the docs for Python Decouple and take a look at the usage and rationale.  There is an example for how to use it with Django.  Follow that to remove the key from settings.

We should also move `DEBUG` to the config file.  Because the file is a string, and `DEBUG` expects a bool, we need to cast it - `config(‘DEBUG’, cast=bool)`

We do this not for security, but so that it can be changed as needed on a development machine, without modifying the source code

Don’t forget to add it to `.env` as well.

Test to make sure it still works and debug as needed.

Before moving on, verify that `.env` is in `.gitignore` and commit.

Code to generate new secret keys from a Python REPL:

```
import random

''.join([random.SystemRandom().choice('abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)') for i in range(50)])  # All one line!
```
-------------------
# Day 2: Admin Interface and SQL

## Admin Interface

Now let’s take a look at the admin functions.

Start the environment and server:
```
pipenv shell
./manage.py runserver
```

Open the page in the web browser and navigate to the admin page:
`localhost:8000/admin`.  You will see a login page, but we don’t have an account
to log in with yet.

To make an admin account, run:
```
./manage.py createsuperuser
```

Add a user `admin` with whatever password you choose.

Although it can be tempting to use a short and easy password for things like
this, it is good practice to use a robust passphrase.  You don’t want to forget
and leave a superuser account with a weak password and have it pass to
production.

Run the server and log into the admin account you just created.  You will be
able to see the automatically generated users and groups from the database, but
our notes are missing.

We need to tell the admin interface which tables we're interested in seeing.

In the `notes/admin.py` file:

```python
from .models import Note
```

and register the `Note` model with the admin site with:

```python
admin.site.register(Note)
```

Return to the site admin page.  `Notes` should now be present.  Try adding
and/or editing a few.

## Migrations with New Fields

It would also be nice to track created and modified dates.  

Open `notes/models.py` and add:

```python
created_at = models.DateTimeField(auto_now_add=True)
last_modified = models.DateTimeField(auto_now=True)
```

The argument we are using determines when and how this information should be
updated:  `auto_now_add` only sets on create, while `auto_now` will set on both
create and update.

In the terminal, make the migration:
```
./manage.py makemigrations
```

You will get the following:
```
You are trying to add the field ‘created_at’ with ‘auto_now_add=True’ to note
without a default; the database needs something to populate existing rows.

1) Provide a one-off default now (will be set on all existing rows)
2) Quit, and let me add a default in models.py
Select an option:
```

Default can sometimes be specified with:
```python
foo = whateverField(default=value)
```

Or you can allow the field to be blank with:
```python
foo = whateverField(blank=True)
```

But this _will not work_ in a `DateTimeField` with `auto_now` or `auto_now_add`
set, so use option 1 with suggested default of `timezone.now`.

Do the migration: `./manage.py migrate`

## Personal (per-user) Notes

Next we want to add the ability to handle multiple users, and allow them to have
their own personal notes.

First, we will create a new model that inherits from another: personal notes.
Open up `notes/models.py`

To access the built-in user functionality:
```python
from django.contrib.auth.models import User
```

We could copy and paste the previous notes class to do this, but a better way is
to have it inherit from it and just add the additional fields we need.

```python
class PersonalNote(Note):   # Inherits from Note!
    user = models.ForeignKey(User, on_delete=models.CASCADE)
```

What this is doing is importing Django’s built in user class model with
something called a _foreign key_ to create a reference to data on another table.
It works sort of like a pointer in C.

`on_delete=models.CASCADE` helps with the integrity of the data.  In relational
databases, one of the principles is to protect consistency.  There shouldn’t be
an item in one table that references the foreign key of something that has been
removed from another.  Check the readme in the repo for more info.

## Under the Hood with SQL

We can take a look in the database with `./manage.py dbshell`.  If you get an
error, you may need to install sqlite3 using your preferred method.

If it is working, the command prompt will change to `sqlite`.

`.tables` will display a list of tables

`pragma table_info(notes_note);` will show column names and types for the table
`notes_note`.

`.headers on` and `.mode column` will adjust some settings to clean up the
presentation if we open a table.

`SELECT * FROM notes_note;` is a sql command that will select all of the columns
in the notes_note table and display the data present.  By convention, sql
commands are often uppercase, but it is actually case insensitive.

All the notes we have created will be displayed.

Be _very_ careful with sql commands.  The command `DROP` will permanently delete
a table and all of the data inside it without warning. _This language is
powerful and has no mercy_.

Type `.exit` or `CTRL-D` to get out of dbshell.

Back in the virtual environment, because we modified the model to add personal
notes, we need to do another migration.

Complete the migration process as before.  

We also want personal notes to show up on the admin page. Open `admin.py` then
import and register the new class.  Remember, you can use tuples for both of
these.  Don’t forget to use the extra parentheses inside the register function.

Take a look at it in `admin`.  It should be the same as before, but now we have
a `user` field that is automatically populated.

We can use the admin interface to add more users in the user table, if we want.

For now, create a personal note for the admin account.

Go back to the sql shell, and take a look at the `notes_personalnote` table.

You’ll need to use the same three commands as above to display the table.  Note
that the info here is very different.  Instead of having everything, it just has
`user_id` and a foreign key `note_ptr_id`, pointing to a record in the full
notes table.

Take a look at the `notes_note` table.  The rest of the data will be here,
listed under the uuid stored in `note_ptr_id`, a reference by the foreign key.
This is why relational databases are relational.

The `user_id` is also a foreign key that points to Django's built-in `auth_user`
table. Run a `SELECT` query to look in that table, as well.

## Django ORM compared to SQL

Drop out of the sqlite shell and open a Python shell.

Import personal notes: `from notes.models import PersonalNote`

Pull the list into a variable: `pn = PersonalNote.objects.all()`

Take a look at the name of the 0th record: `pn[0].user`.  Try other fields as
well.

Django lets us access information that is in multiple tables relatively easily.
The sql details are hidden from us (in a good way!).  It does all of the under
the hood operations for us.