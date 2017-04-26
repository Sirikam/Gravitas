Gravitas - README.txt
===============
================================================================================
Gravitas is an app/bot that will make the users life as a student easier. 
Professors can share lecture materials and post quizzes related to the 
lecturematerial. The user also have access to their schedule. 


Prerequisites and installing
===============

Gravitas was made in PyCharm with Django and Bootstrap framework.
https://www.jetbrains.com/pycharm/
-Click "download now"
-Click on "download" under "community" (if you are a student or professor 
at NTNU you can choose "professional")
-Open the file
-follow the steps in the installing-window

https://www.djangoproject.com/
http://getbootstrap.com/

Software to be installed in the project
=======================================
There is a virtual server added to the project called Gravenv, if that fails, follow instruction below

If you use pycharm, open file>settings>project interpreter, and create a
virtualenv.

below is a list of plugins to install
=====================================
Plugin                  Version
-------------------------------------
Django              	1.11
appdirs             	1.4.3
coverage            	4.4b1
django-model-utils  	2.6.1
django-registration 	2.2
django-widget-list  	0.10.0
django-widget-tweaks   	1.4.1
olefile             	0.44
packaging           	16.8
pillow              	4.0.0
pip                 	9.0.1
pluggy              	0.4.0
psycopg2            	2.7.1
py	                  	1.4.33
pyparsing              	2.2.0
pytz                	2016.10
requests            	2.13.0
setuptools          	34.3.3
six                 	1.10.0
tox                 	2.6.0
virtualenv          	15.1.0

To install pip in console:

download the get-pip.py script(https://raw.github.com/pypa/pip/master/contrib/get-pip.py), save it locally,
then run it using Python as shown below:

"PS C:\> python get-pip.py
Downloading/unpacking pip
Downloading/unpacking setuptools
Installing collected packages: pip, setuptools
Successfully installed pip setuptools
Cleaning up...
PS C:\>"

To install plugins with pip in console write: pip install <plugin_name>
Example C:\Users\Admin\Gravitas> pip install virtualenv

Tests
===============
For use of the Coverage tool, make sure that the coverage is installed in the project,
then rightclick the folder and select run with coverage. Create a django test, and select your
project interpreter as teh test interpreter. Run the test.


How to run the app/bot
===============
To run the server and use the app/bot you must follow these steps.
Open terminal and go to the project directory, then write: python manage.py runserver
open a web-browser and write in the URL field: 127.0.0.1:8000


License
===============
Please see the file called LICENSE.md 


Acknowledgments
===============
-->Hat tip to anyone who's code was used<--
-->Inspiration<--
Quiz - This is a configurable quiz app for Django, developed by
Tom Walker ([tomwalker](https://github.com/tomwalker)).


Contributors
===============
Bendik Harto Seim
Siri H. Ulltveit-Moe
Steffen Helgeland
Julie Davidsen

For bugs and other consernes about the site, please contact us.