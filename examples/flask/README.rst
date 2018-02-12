====================
Example for Flask
====================

Setup
======

::

 $ pip install uadetector
 $ pip install Flask

Run
===========

::

 $ FLASK_APP=main.py flask run

You can access http://127.0.0.1:5000. and get output like bellow.

::

 {
   "device_type": "pc",
   "os": "Mac OSX",
   "browser": "Chrome",
   "from_pc": true,
   "from_smartphone": true
 }
