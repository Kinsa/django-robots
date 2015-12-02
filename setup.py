from setuptools import setup, find_packages


setup(
    name='django-robots',
    version=1.0,
    packages=find_packages(exclude=["test_project"]),
    install_requires=['Django>=1.7'],
    author='Joe Bergantine',
    author_email='jbergantine@gmail.com',
    description="robots.txt File Generation Django",
    url='https://github.com/jbergantine/django-robots',
    download_url='https://github.com/jbergantine/django-robots/tarball/1.0',
    license='New BSD License',
    platforms=['any'],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Utilities',
    ],
    test_suite="runtests.runtests",
    include_package_data=True,
)
