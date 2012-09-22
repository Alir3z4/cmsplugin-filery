#!/usr/bin/env python

from distutils.core import setup

setup(
    name='cmsplugin_filery',
    version='0.5.2',
    author='Alireza Savand',
    author_email='alireza.savand@gmail.com',
    description = 'Image gallery based on django-filer',
    packages=['cmsplugin_filery',],
    package_dir={'cmsplugin_filery': 'cmsplugin_filery'},
    package_data={'cmsplugin_filery': ['templates/*/*']},
    provides=['cmsplugin_filery'],
    include_package_data=True,
    install_requires = ['django-inline-ordering>=0.1.1', 'easy-thumbnails',
                        'django-filer']
)
