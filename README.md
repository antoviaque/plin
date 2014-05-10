Installation
============

Install the dependencies:

```
sudo pip install -r requirements.txt
```

Then update the database:

```
./manage.py syncdb && ./manage.py migrate
```

If it's the first time you run it, it will ask you if you want to create a user - answer 'yes', as this will grant admin rights to this user, which you will need to add books.

Running the server
==================

Start the local server with:

```
./manage.py runserver
```

Then go to [http://localhost:8000/](http://localhost:8000)
