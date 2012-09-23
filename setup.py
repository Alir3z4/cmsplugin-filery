from distutils.core import setup

setup(
    name='cmsplugin-filery',
    version=".".join(map(str, __import__('cmsplugin_filery').__version__)),
    author='Alireza Savand',
    author_email='alireza.savand@gmail.com',
    url='http://pypi.python.org/pypi/cmsplugin-filery',
    description = 'Image gallery based on django-filer',
    long_description=open('README.rst').read(),
    license='LICENSE',
    keywords=[
        'django',
        'django-cms',
        'web',
        'cms',
        'cmsplugin',
        'plugin',
        'image',
        'gallery',
        ],
    packages=['cmsplugin_filery', 'cmsplugin_filery.migrations'],
    package_dir={'cmsplugin_filery': 'cmsplugin_filery'},
    package_data={'cmsplugin_filery': ['templates/*/*']},
    provides=['cmsplugin_filery'],
    include_package_data=True,
    install_requires = [
        'django',
        'django-cms',
        'easy-thumbnails',
        'django-filer'
    ],
    platforms='OS Independent',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Programming Language :: Python',
        'Framework :: Django',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Topic :: Software Development'
    ],
)
