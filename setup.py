#!/usr/bin/env python

from distutils.core import setup

setup(
    name='cmsplugin_gallery_filer',
    version='0.5.2',
    author='GISA Elkartea',
    author_email='kontaktua@gisa-elkartea.org',
    url='http://lagunak.gisa-elkartea.org/projects/cmsplugin-gallery-filer',
    description = 'DjangoCMS image gallery plugin with drag&drop '
                  'reordering in admin, support for thumbnails and '
                  'jQueryTOOLS overlay. Fork to use django-filer',
    packages=find_packages(),
    provides=['cmsplugin_gallery', ],
    include_package_data=True,
    install_requires = ['django-inline-ordering>=0.1.1', 'easy-thumbnails',
                        'django-filer']
)
