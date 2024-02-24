import os

from setuptools import setup, find_packages

description = "robots.txt File Generation Django"
long_description = description

if os.path.exists('README.rst'):
    long_description = open('README.rst').read()

setup(
    name='django-robots',
    version='1.1.3',
    packages=find_packages(exclude=["tests"]),
    install_requires=[
        'Django>=1.11'
    ],
    author='Kinsa Creative Incorporated',
    author_email='enquiries@kinsa.cc',
    description=description,
    long_description=long_description,
    url='https://github.com/Kinsa/django-robots',
    download_url='https://github.com/Kinsa/django-robots/tarball/1.1.3',
    license='New BSD License',
    platforms=['any'],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: 1.11',
        'Framework :: Django :: 2.1',
        'Framework :: Django :: 2.2',
        'Framework :: Django :: 3.0',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'License :: OSI Approved :: BSD License',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
    test_suite="runtests.runtests",
    include_package_data=True,
)
