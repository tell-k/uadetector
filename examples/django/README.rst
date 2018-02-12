====================
Example for Django
====================

Setup
======

::

 $ pip install uadetector
 $ pip install Django

Run
===========

::

 $ python manage.py runserver

You can access http://127.0.0.1:8000. and get output like bellow.

::

 {
   "device_type": "pc",
   "os": "Mac OSX",
   "browser": "Chrome",
   "from_pc": true,
   "from_smartphone": true
 }
