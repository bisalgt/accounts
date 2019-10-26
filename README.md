pipenv --python 3.7

pipenv shell (everyday you run your project)

pipenv install django==2.2.2
django-admin startproject news_portal .



To run project:

python manage.py runserver

To see all the cammand for manage.py:

python manage.py

To start new app in django
python manage.py startapp news


#########################
GIT commands
##########################

#create new branch:

git branch branch_name

#To switch into any branch

git checkout template-setup

#Create new branch and checkout into it.

git checkout -b template-setup


# Delete a branch

git branch -D template-setup

#if you have created a new file you need to track it. For this run following command:

git add . 

#commit

git commit -m "you commit message"

git commit -am "create models for news"



#MANAGE.PY commands
==========================

#DB realated commands
when you make or update models, run following command:

python manage.py makemigrations

#To migrate models into physical database run following command:

python manage.py migrate

#To see the generated queries:
if 0001_initial.py is my migration file in news app then run following command:

python manage.py sqlmigrate news 0001

# If you have image field in models you need to install image library package called Pillow:

pipenv install Pillow

#create superuser in django

python manage.py createsuperuser