from setuptools import find_packages, setup

setup(
    name='django-core',
    packages=find_packages(include=['django-core']),
    url="https://github.com/Arpitpatel1771/django-core.git",
    install_requires = [
        "asgiref==3.7.2",
        "Django==4.2.6",
        "djangorestframework==3.14.0",
        "install==1.3.5",
        "pytz==2023.3.post1",
        "sqlparse==0.4.4",
        "typing_extensions==4.8.0",
    ],
    version='1.0.0',
    description='core library for all my django projects',
    author='Me',
)