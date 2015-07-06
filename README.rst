This assumes that python 2.7.x, pip, virutalenv and virtualenvwrapper are installed already

If you need to install virtualenv or virtualenvwrapper, these may help
http://linuxconfig.org/setting-up-the-python-virtualenv-development-environment-on-debian-linux
http://virtualenvwrapper.readthedocs.org/en/latest/install.html


Once you've unzipped the zip file to your preferred directory, the following commands should get you
up and running.

	mkvirtualenv django-api

	workon django-api

	cd /path/to/django_api/manage.py

	pip install -r requirements.txt

	python manage.py runserver_plus


You can then use your browser or the command-line tool curl (among others) to issue requests to the server.


Curl examples:

curl --request GET "http://localhost:8000/api?word=fizz&max_value=5"
output:
{"status":"ok","numbers":[3]}

curl --request GET "http://localhost:8000/api?word=fizzbuzz&max_value=90"
output:
{"status":"ok","numbers":[15,30,45,60,75,90]}


Browser examples:
http://localhost:8000/api?word=fizz&max_value=5
Displays:
{"status":"ok","numbers":[3]}


python manage.py test

