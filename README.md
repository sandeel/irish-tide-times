Irish Tide Times
==================

Project for Cloud Computing module National College of Ireland. Student no. x11105089

A Django application for a website which offers Irish tide times by SMS.

Installation
------------

Install git

    sudo apt-get install git

install the requirements from requirements/txt

    pip install Django==1.5 South>=0.7.5 django-extensions==1.2.0 beautifulsoup4 requests twilio

install nginx

    sudo apt-get install nginx

Clone the repo

    git clone https://github.com/sandeel/irish-tide-times.git
    cd irish-tide-times

copy the nginx config file from the repository

    sudo cp nginx.conf /etc/nginx/nginx.conf

make the gunicorn script executable

    sudo chmod +x app/run_gunicorn.sh 

run the server
    ./run_gunicorn.sh
