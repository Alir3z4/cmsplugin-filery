=======================
cmsplugin-filery
=======================

cmsplugin-filery adds simple & minimal image gallery for django-cms.
And it's based on django-filer.

Features:

- Uses django-filer for storing images.
- Ordering images

Please not that cmsplugin-filery requires:

- easy-thumbnails http://pypi.python.org/pypi/easy-thumbnails/
- django-filer http://pypi.python.org/pypi/django-filer/

Installation
============

#. `pip install cmsplugin-filery`
#. Add `'cmsplugin_filery'` to `INSTALLED_APPS` (if necessary)
#. Run `syncdb` or `migrate cmsplugin_filery` if using South


Usage
=====

Just ovveride the original filery's gallery templates,
like when you overide admin templates.

::
    templates/cmsplugin_filery/gallery.html

Bugs & Contribution
===================

Please use Github to report bugs, feature requests and submit your code:
https://github.com/Alir3z4/cmsplugin-filery/issues
