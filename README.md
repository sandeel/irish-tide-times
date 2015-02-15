Irish Tide Times
==================

A Django application for a website which offers Irish tide times by SMS.

Themed using Bootstrap.

[Irish Tide Times](http://www.irishtidetimes.com)


Installation
------------

Install requirements

    sudo apt-get install git nginx python-setuptools python-dev build-essential

Install pip

    sudo easy_install pip

Install the Python requirements from requirements.txt

    sudo pip install Django==1.5 South>=0.7.5 django-extensions==1.2.0 beautifulsoup4 requests twilio gunicorn

Clone the repo

    git clone https://github.com/sandeel/irish-tide-times.git
    cd irish-tide-times

Copy the nginx config file found inside the repo

    sudo cp nginx.conf /etc/nginx/nginx.conf

Make the gunicorn script executable

    cd app
    sudo chmod +x run_gunicorn.sh 

Edit the following line in the wsgi.py file to point to the absolute location of the irish-tide-times folder

    sys.path.append('/home/ubuntu/irish-tide-times')

run the server
    ./run_gunicorn.sh

