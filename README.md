# Movie - Api
Movie Fav is social network plattform for everyone who loves movies and series. 
The primary goals of the web app are to:

1) As a user you can review movies or series. Tell about actors, about the soundtrack or share other thoughts you have. You get tips from other users about movies or series you missed.

2) Deliver a simple and colorful user experience, suitable for users in all ages. 


This is the repository for the React backend of Movie Fav.

#### DEPLOYED BACKEND API [LINK](https://movie-fav-project-5.herokuapp.com/)
#### DEPLOYED FRONTEND [LINK - LIVE SITE](https://moviefav-1a8485e84849.herokuapp.com/)
#### DEPLOYED FRONTEND [REPOSITORY](https://github.com/HannaBerggren/Movie-Fav/)

## CONTENTS

* [Project Structure](#project-structure)
  * [Agile workflow](#agile-workflow)
  * [User Stories](#user-stories)
* [Database Design](#databasedesign)
  * [Models](#models)
  * [ERD](#erd)
* [Technologies Used](#technologies-used)
  * [Languages](#languages)
  * [Frameworks and software](#frameworks-and-software)
  * [Libraries](#libraries)
* [Testing](#testing)
* [Deployment](#deployment)
    * [How to Fork](#how-to-fork)
    * [How to Clone](#how-to-clone)
* [Credits](#credits)
  * [Code Used](#code-used)
  * [Online Resources](#online-resources)
  * [Acknowledgments](#acknowledgments)


# **Project Structure**
The overall structure of the project was modelled on the [drf-api](https://github.com/Code-Institute-Solutions/drf-api) walkthrough due to time limitations.

I've tried to customize the walkthrough where possible to fit my own project.

## Agile Workflow
I built this API using Agile principles from the start by creating user stories for the front end application for the developer/superuser to follow.
The user stories were used to inform wireframes mapping out the intended functionality and structure through the app.
For more details see the [repo for the frontend React application](https://github.com/HannaBerggren/Movie-Fav)

## User Stories
Here you will find the [GitHub Issues](https://github.com/HannaBerggren/Movie-Fav/tree/main/.github/ISSUE_TEMPLATE) for this project.

[Back to top](<#contents>)

# **Database Design**

## Models
The following models was created by me for the Movie api:
 * User 
 * Profile (automatically created when a user Is created)
 * Posts (A post by a user with gardening ideas)
 * Comment (To make a comment on a post)
 * Likes (To indicate if a user likes an post)
 * Follow (For users to follow other users of the site)

[Back to top](<#contents>)

## Relationship diagram
The relationship between all of the above models is summarized in the following diagram
[ERD](https://lucid.app/lucidchart/b5a0f643-c2ac-4f6f-b554-8cb8b9a1334c/edit?viewport_loc=-11%2C-32%2C2050%2C1779%2C0_0&invitationId=inv_5fb23692-d67e-469c-9a8a-e9ba6feb94fb).

[Back to top](<#contents>)

# **Technologies Used**

## Languages
 * [Python](https://en.wikipedia.org/wiki/Python_(programming_language)) - Provides the functionality for the DRF backend framework.

[Back to top](<#contents>)

## Frameworks and Software

* [Django Rest Framework](https://www.django-rest-framework.org/) - A framework for building web API's
* [PEP8 Validation](https://pypi.org/project/pep8/) - pep8 is a tool to check your Python code against some of the style conventions in PEP 8.
* [Github](https://github.com/) - Used to host the repository, store the commit history and manage the project board containing user stories and bug reports.
* [Heroku](https://en.wikipedia.org/wiki/Heroku) - A cloud platform that the application is deployed to.
* [Cloudinary](https://cloudinary.com/) - A service that hosts image files in the project.
* [Lucidchart](https://drawsql.app/)  - Create the Entity Relationship Database schema (ERD).
* [Iconfinder](https://www.iconfinder.com/) - A platform for icons.
* [ILOVEIMG](https://www.iloveimg.com/) - An online photo editor, used to resize images.

[Back to top](<#contents>)

## Libraries
* [asgiref](https://pypi.org/project/asgiref/)
* [cloudinary](https://pypi.org/project/cloudinary/) 
* [dj-database-url](https://pypi.org/project/dj-database-url/0.5.0/) 
* [dj-rest-auth](https://pypi.org/project/dj-rest-auth/) 
* [Django](https://pypi.org/project/Django/) 
* [django-allauth](https://pypi.org/project/django-allauth/)
* [django-cloudinary-storage](https://pypi.org/project/django-cloudinary-storage/) 
* [django-cors-headers](https://pypi.org/project/django-cors-headers/)
* [django-filter](https://pypi.org/project/django-filter/)
* [django-rest-framework](https://pypi.org/project/djangorestframework/)
* [djangorestframework-simplejwt](https://pypi.org/project/djangorestframework-simplejwt/)
* [gunicorn](https://pypi.org/project/gunicorn/)
* [oauthlib](https://pypi.org/project/oauthlib/) 
* [pillow](https://pypi.org/project/Pillow/8.2.0/) 
* [psycopg2](https://pypi.org/project/psycopg2/)
* [PyJWT](https://pypi.org/project/PyJWT/) 
* [python3-openid](https://pypi.org/project/python3-openid/) 
* [pytz](https://pypi.org/project/pytz/) 
* [requests-oauhlib](https://pypi.org/project/requests-oauthlib/) 
* [sqlparse](https://pypi.org/project/sqlparse/)

[Back to top](<#contents>)

# **Testing**
### Manual Testing:
1. Manually verified each url path created works & opens without error.
2. Verified that the CRUD functionality is available in each app via the development version: Comments, Contact, Followers, Likes, Posts and Profile.
 - Checked this by going to each link.
 - Creating a new item.
 - Checking new item URL path. 
 - Editing the item (not available for Likes, Followers or Users)
 - Deleting the item (Not available for Users or Profiles)
3. Ensured search feature for Posts or User, returns results. 

### Unfixed Bugs
- Not that I'm aware of.

[Back to top](<#contents>)

# **Deployment & Local Development**
  * [Deployment](#deployment)
  The project was deployed to [Heroku](https://www.heroku.com). To deploy, please follow the process below:

  1. To begin with create a GitHub repository from the [Code Institute template](https://github.com/Code-Institute-Org/gitpod-full-template) by following the link and then click 'Use this template'.

2. Fill in the details for the new repository and then click 'Create Repository From Template'.

3. When the repository has been created, click on the 'Gitpod' button to open it in the GitPod Editor.

4. Install Django and the supporting libraries that are needed, using the following commands in the terminal:

* ```pip3 install 'django<4' gunicorn```
* ```pip3 install 'dj_database_url psycopg2```
* ```pip3 install 'dj3-cloudinary-storage```

5. When Django and the libraries are installed create a requirements file.

* ```pip3 freeze --local > requirements.txt``` - This will create and add required libraries to requirements.txt


6. It's time to create the project.

* ```django-admin startproject YOUR_PROJECT_NAME .``` - This will create the new project.

7. Now when the project is created lets create the applications. My project consists the following apps; Comments, Followers, Likes, Posts and Profiles.

* ```python3 manage.py startapp APP_NAME``` - This will create an application

8. Add the applications to settings.py in the INSTALLED_APPS list.

8. It is time to do our first migration and run the server to test that everything works as expected. Please write the commands below.

* ```python3 manage.py makemigrations``` - This will prepare the migrations
* ```python3 manage.py migrate``` - This will migrate the changes
* ```python3 manage.py runserver``` - Runs the server. Click the open browser button that will be visible after the command is run to test it.

9. Next we create our application on Heroku, attach a database, prepare our environment and settings.py file and setup the Cloudinary storage for our static and media files.

* To create a new app: once signed into your [Heroku](https://www.heroku.com/) account, click on the button labeled 'New'. 

10. Choose a unique app name, choose your region and click 'Create app".

11. Next we need to connect an external PostgreSQL database to the app from [ElephantSQL](https://customer.elephantsql.com/login).  Once logged into your ElephantSQL dashboard, you click 'Create New Instance' to create a new database. Give the database a: 
* Name
* Tiny Turtle Free Plan
* Selected data center near you and click 'Create Instance'. Return to your ElephantSQL Dashboard, and click into your new database instance. Copy the Database URL and head back to Heroku.

12. Back in your Heroku app settings, click on the 'Reveal Config Vars' button. Create a config variable called DATABASE_URL and paste in the URL you copied from ElephantSQL. This connects the database into the app. 

13. Go back to GitPod and create a new env.py in the top level directory. Then add these rows.

* ```import os``` - This imports the os library
* ```os.environ["DATABASE_URL"]``` - This sets the environment variables.
* ```os.environ["SECRET_KEY"]``` - Here you can choose whatever secret key you want.

14. Back in the Heroku Config Vars settings, create another variable called SECRET_KEY and copy in the same secret key as you added into the env.py file. Don't forget to add this env.py file into the .gitignore file so that it isn't commited to GitHub for other users to find. 

15. Now we have to connect to our environment and settings.py file. In the settings.py, add the following code:

```import os```

```import dj_database_url```

```if os.path.isfile("env.py"):```

```import env```

16. In the settings file, remove the insecure secret key and replace it with:
```SECRET_KEY = os.environ.get('SECRET_KEY')```

17. Comment out the old database settings in the settings.py file (this is because we are going to use the postgres database instead of the sqlite3 database).

Instead, we add the link to the DATABASE_URL that we added to the environment file earlier.

18. Save all your fields and migrate the changes again.

```python3 manage.py migrate```

19. Now we can set up [Cloudinary](https://cloudinary.com/users/login) (this is where we will store our static files). First you need to create a Cloudinary account and from the Cloudinary dashboard copy the API Environment Variable.

20. Go back to the env.py file in Gitpod and add the Cloudinary url (it's very important that the url is correct):

```os.environ["CLOUDINARY_URL"] = "cloudinary://************************"```

21. Head back to Heroku and add the Cloudinary url in Config Vars. Add a disable collectstatic variable to get our first deployment to Heroku to work.

22. Back in the settings.py file, we now need to add our Cloudinary Libraries we installed earlier to the INSTALLED_APPS list. Here it is important to get the order correct.

* cloudinary_storage
* django.contrib.staticfiles
* cloudinary

23. For Django to be able to understand how to use and where to store static files we need to add some extra rows to the settings.py file.

24. To be able to get the application to work through Heroku we also need to add our Heroku app and localhost to the ALLOWED_HOSTS list:

```ALLOWED_HOSTS = ['', 'localhost']```

25. Create the basic file directory in Gitpod.

* Create a file called **Procfile* and add the line ```web: gunicorn PROJ_NAME.wsgi?``` to it.

26. Save all the files and prepare for the first commit and push to Github by writing the lines below.

* ```git add .```
* ```git commit -m "Deployment Commit```
* ```git push```

27. It's time for deployment. Scroll to the top of the settings page in Heroku and click the 'Deploy' tab. For deployment method, select 'Github'. Search for the repository name you want to deploy and then click connect.

28. Scroll down to the manual deployment section and click 'Deploy Branch'. I hope that the deployment went all good!

[Back to top](<#contents>)
  
## How to Fork
By forking the GitHub account it is possible to make an independent copy of a GitHub Repository.  
The copy can then be viewed and it is also possible to make changes in the copy without affecting the original repository. To fork the repository, follow these steps:

1. After logging in to GitHub, locate the repository. On the top right side of the page there is a 'Fork' button. Click on the button to create a copy of the original repository.

[Back to top](<#contents>)

## How to Clone

1. When you are in the repository, find the code tab and click it.
2. To the left of the green GitPod button, press the 'code' menu. There you will find a link to the repository. Click on the clipboard icon to copy the URL.
3. Use an IDE and open Git Bash. Change directory to the location where you want the cloned directory to be made.
4. Type 'git clone', and then paste the URL that you copied from GitHub. Press enter and a local clone will be created.
5. To be able to get the project to work you need to install the requirements. This can be done by using the command below:

* ```pip3 install -r requirements.txt``` 

6. The next step is to set up the environment file so that the project knows what variables that needs to be used for it to work. Environment variables are usually hidden due to sensitive information. It's very important that you don't push the env.py file to Github, this can be secured by adding env.py to the .gitignore-file. The variables that are declared in the env.py file needs to be added to the Heroku config vars. Don't forget to do necessary migrations before trying to run the server.

* ```python3 manage.py migrate``` - This will do the necessary migrations.
* ```python3 manage.py runserver``` - If everything i setup correctly the project is now live locally.

[Back to top](<#contents>)

# **Credits**
## Code Used
  Code Institute DRF Tutorial Project, was used through out this project as a basis for the creation of this API
* CREDIT: Code Institute DRF-API Tutuorial Project
-   [Code Institute, drf-api](https://github.com/Code-Institute-Solutions/drf-api)

[Back to top](<#contents>)

## Online Resources
* [Django Documentation](https://docs.djangoproject.com/)
* [Django REST Documentation](https://www.django-rest-framework.org/)
* [Python Documentation](https://docs.python.org/)
* [Youtube tutorials](https://www.youtube.com/)

[Back to top](<#contents>)

## Acknowledgments
* Code Institute for your tutorsupport
* My family and friends for support
* My cousin for her tremendous support

[Back to top](<#contents>)
