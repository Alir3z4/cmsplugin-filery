=================
cmsplugin-filery
=================

.. contents:: Table of contents

Overview
=========
cmsplugin-filery adds simple & minimal image gallery for django-cms.
And it's based on django-filer.

Features:

- Uses django-filer for storing images.
- Ordering images

Please not that cmsplugin-filery requires:

- easy-thumbnails 
    http://pypi.python.org/pypi/easy-thumbnails/
- django-filer
    http://pypi.python.org/pypi/django-filer/

Installation
============

#. `pip install cmsplugin-filery`
#. Add ``cmsplugin_filery`` to ``INSTALLED_APPS`` (if necessary)
#. Run ``syncdb`` or ``migrate cmsplugin_filery`` if using **South**


Usage
=====

Just ovveride the original filery's gallery templates,
like when you overide admin templates.

::
    
    templates/cmsplugin_filery/gallery.html

Additionally, you can add your templates to ``templates/cmsplugin_filery/``  and register them in ``settings.py``.  
This will make the templates available for selection in the user interface.

::

    # In the templates directory
    templates/cmsplugin_filery/gallery_1.html
    templates/cmsplugin_filery/gallery_2.html

::

    # In settings.py
    CMSPLUGIN_FILERY_TEMPLATES = (
        ('gallery_1.html', 'My First Gallery'), 
        ('gallery_2.html', 'My Second Gallery'), 
    )


Bugs & Contribution
===================

Please use Github to report bugs, feature requests and submit your code:

https://github.com/Alir3z4/cmsplugin-filery/issues
