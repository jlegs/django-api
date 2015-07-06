This assumes python 2.7.x, pip, virutalenv and virtualenvwrapper are installed already

If you need to install virtualenv or virtualenvwrapper, these may help
http://linuxconfig.org/setting-up-the-python-virtualenv-development-environment-on-debian-linux
http://virtualenvwrapper.readthedocs.org/en/latest/install.html






	mkvirtualenv django-api
	workon django-api
	pip install -r requirements.txt
	python manage.py runserver_plus




curl --request GET "http://localhost:8000/api?word=fizz&max_value=5"
output:
{"status":"ok","numbers":[3]}

curl --request GET "http://localhost:8000/api?word=fizzbuzz&max_value=90"
output:
{"status":"ok","numbers":[15,30,45,60,75,90]}



python manage.py test

