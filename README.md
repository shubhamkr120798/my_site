# my_site
Registeration Form created using Django and sqllite or MongoDB(as per use case)

By Default : sqllite will run with the above code.
For Running MongoDb : Go to settings.py and change Databases section to :-
#If your database is in your local machine
DATABASES = {
   ‘default’: {
      ‘ENGINE’: ‘djongo’,
      ‘NAME’: ‘your-db-name’,
   }
}
If your database is on any server then :~
DATABASES = {
   ‘default’: {
      ‘ENGINE’ : ‘djongo’,
      
       ‘NAME’ : ‘your-db-name’, #as named on server
      
       'HOST' : 'mongodb://<dbuser>:<dbpassword>@ds259144.mlab.com:59144/<db-name>',
#that is your connection link with your username,password and db name,here i created a db using mlabs of mongodb
       'USER' : '<dbuser>',
       'PASSWORD' : '<dbpassword>',

   }
}

To Run the code :
clone this to your computer and run the following commands :
1. cd to went to mysite director : cd mysite
2. python manage.py make migrations registeration
3. python manage.py migrate
4. python manage.py runserver
After these commands , registeration form will be active and run on the localhost .




Database : 
All the verified users data will be stored in database(sql or mongodb as per requirement ).
Two Models for the database is there :
collection 1 : user : {name,email,password}
collection 2 : system: { ip}
Collection 1 stores the user's information 
Collection 2 stored the ip addr of the system which are registering on the  website



Future works that are left :

To create a function( Update) ; that clears the system database containing ip addr of system  after every 24 hrs(as described in the assignment)

