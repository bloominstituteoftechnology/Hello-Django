to get into the shell, run `pipenv shell`
Once in shell, run `./manage.py runserver` and open localhost - you should see the django homepage
Navigate to `localhost:####/admin` to open the admin page

() Creating a user:
To create a user, run `./manage.py createsuperuser`, and enter in a username, email, and password. (admin, email, adminpassword)

Foreign Keys are ways to point or reference items in other models or other tables (such as a note pointing to a specific user in another table). They can be made 

<!-- go back and add note drom day 1 -->


() Models
Models frame the items that will be held in the database. Once created, the app needs to be added to the `settings.py` file in the primary db, and then they must be migrated with `./manage.py makemigrations`, and then finalized with `./manage.py migrate`.

() Subclasses
When declaring classes, you may want to have another distinct class that shares all of another's traits except it adds a new field. In this case, you can simply declare a new class, but pass it the other class as the parent:
    class Note(models.Model)
        user = ...
        pass = ...
    
    class PersonalNote(Note)
        zip = ... 
    

() APIs in Django
enter `pipenv shell`, `pipenv install djangorestframework`

you can test APIs with `curl URLEndpoint`
