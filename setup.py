from distutils.core import setup

setup(
    name='cmsplugin-filery',
    version=".".join(map(str, __import__('cmsplugin_filery').__version__)),
    author='Alireza Savand',
    author_email='alireza.savand@gmail.com',
    description = 'Image gallery based on django-filer',
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
    packages=['cmsplugin_filery',],
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
)
