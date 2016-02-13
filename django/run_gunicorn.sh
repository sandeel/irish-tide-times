gunicorn wsgi:application --log-file=- -b 0.0.0.0:8080 -w 9 -t 60 --max-requests=500 --preload

