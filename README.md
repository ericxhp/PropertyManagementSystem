Example project for: https://bitbucket.org/pigletto/django-datatables-view

Installation:

1. Change to project directory
    
    ````
    $ cd django-datatables-view-example/
    ````
    
2. Create and activate virtualenv: 

    ````
    $ virtualenv env
    $ source env/bin/activate
    ````
   
3. Install required packages

    ````
    pip install -r requirements.txt
    ````
    
4. Create database
    ```` 
    ./manage.py migrate
    ````

5. Create superuser to have database filled with some data
    ```` 
    ./manage.py createsuperuser
    ````

6. Run
    ````
    ./manage.py runserver
    ````

Visit http://localhost:8000

To add some records to database go to: http://localhost:8000/admin and add new users.
