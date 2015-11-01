Irish Tide Times
==================

A Django application for a website which offers Irish tide times by SMS.

Themed using Bootstrap.

[Irish Tide Times](http://www.irishtidetimes.com)


Installation
------------

Install requirements

    sudo apt-get update
    sudo apt-get install git nginx python-setuptools python-dev build-essential python-pip

Clone the repo

    git clone https://github.com/sandeel/irish-tide-times.git
    cd irish-tide-times
    
Install the Python requirements from requirements.txt

    sudo pip install -r requirements.txt

Copy the nginx config file found inside the repo

    sudo cp nginx.conf /etc/nginx/nginx.conf

Make the gunicorn script executable

    cd app
    sudo chmod +x run_gunicorn.sh 

Edit the following line in the wsgi.py file to point to the absolute location of the irish-tide-times folder

    sys.path.append('/home/ubuntu/irish-tide-times')

run the server
    ./run_gunicorn.sh

