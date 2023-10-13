from setuptools import find_packages, setup

setup(
    name="core_django",
    packages=find_packages(include=["core_django", "auth"]),
    url="https://github.com/Arpitpatel1771/django-core.git",
    install_requires=[
        "asgiref==3.7.2",
        "certifi==2023.7.22",
        "charset-normalizer==3.3.0",
        "Django==4.2.6",
        "djangorestframework==3.14.0",
        "idna==3.4",
        "install==1.3.5",
        "pytz==2023.3.post1",
        "requests==2.31.0",
        "sqlparse==0.4.4",
    ],
    version="1.0.0",
    description="core library for all my django projects",
    author="Me",
)
