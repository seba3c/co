# co
Install instructions

1) Create a python virtual env for python3.5
* mkvirtualenv co --python=/usr/bin/python3.5

http://docs.python-guide.org/en/latest/dev/virtualenvs/

2) Install python dependencies using pip (virtualenv must be active)
* pip install -r requirements/base.txt

3) Initialize django database
* python manage.py migrate

NOTE: you should need to export "DJANGO_SETTINGS_MODULE=config.settings.dev" before run the above
command

Time spent in assignment

* 15hs approximately 

Assumptions

* Every machine on the intranet has the capability to execute python scripts to get system
information

Requirements not covered

* Get Windows security alerts
* I mark in the code (with TODO tags) some tech debts and pending works
* A better handling of error and exceptions
* Encryption (Anyway, reading some paramiko documentation,channels with remote host are already encrypted)

Issues faced

* I have not used paramiko lib before. I had to learn the basis on the go.

Feedback

* I used some django capabilities to implement some of the requirements, in particular:
** Django models to persist data from remote hosts
** Django email backend to send email. I used "django.core.mail.backends.console.EmailBackend", to simulate email sending
** Django command to init the host data collection

Run the system

* python manage.py test (to run unitets)
* python manage.py collect_stats (to run the remote host data collection)

* config file is in config/settings/clients_config.xml

