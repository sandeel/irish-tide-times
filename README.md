Irish Tide Times
==================

A Django application for a website which offers Irish tide times by SMS.

Installation
------------

Install git

    sudo apt-get install git

Follow instructions here to set up Python virtual environment

http://dimamoroz.com/blog/2-python-virtual-environment-ubuntu/

install the requirements from requirements/txt

Clone the repo
    git clone https://github.com/sandeel/irish-tide-times.git

install nginx
    sudo apt-get install nginx

copy the nginx config file from the repository
    sudo cp nginx.conf /etc/nginx/nginx.conf

make the gunicorn script executable
    sudo chmod +x app/run_gunicorn.sh 

