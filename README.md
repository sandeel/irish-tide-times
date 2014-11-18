Irish Tide Times
==================

Project for Cloud Computing module National College of Ireland. Student no. x11105089

A Django application for a website which offers Irish tide times by SMS.

Installation
------------

Install git

    sudo apt-get install git

install nginx

    sudo apt-get install nginx

sudo apt-get install python-setuptools python-dev build-essential
sudo easy_install pip

install the requirements from requirements/txt

    sudo pip install Django==1.5 South>=0.7.5 django-extensions==1.2.0 beautifulsoup4 requests twilio gunicorn

Clone the repo

    git clone https://github.com/sandeel/irish-tide-times.git
    cd irish-tide-times

copy the nginx config file from the repository

    sudo cp nginx.conf /etc/nginx/nginx.conf


make the gunicorn script executable

    cd app
    sudo chmod +x run_gunicorn.sh 

Edit the following line in the wsgi.py file to point to the absolute location of the irish-tide-times folder

    sys.path.append('/home/ubuntu/irish-tide-times')

run the server
    ./run_gunicorn.sh
