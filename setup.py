from setuptools import setup

setup(name='QueueMe',
      version='1.0',
      description='Information Hub for League Users',
      author='Larry Liu',
      author_email='TBD',
      url='TBD',
      install_requires=['Flask >= 0.10.0, < 0.11.0',
                        'Flask-Login >= 0.2.0, < 0.3.0',
                        'Flask-Migrate >= 1.4.0, < 1.5.0',
                        'Flask-SQLAlchemy >= 2.0, < 3.0',
                        'Flask-SSLify >= 0.1.5, < 0.2.0',
                        'Flask-Script >= 2.0.5, < 2.1.0',
                        'Flask-WTF >= 0.11, < 0.12',
                        'Jinja2 >= 2.7.3, < 2.8.0',
                        'MySQL-python >= 1.2.3, < 1.3.0',
                        'SQLAlchemy >= 1.0.4, < 1.1.0',
                        'WTForms >= 2.0.2, < 2.1.0',
                        'simplejson >= 3.7.2, < 3.8.0',
                        'urllib3 >= 1.8.3, < 1.9.0']
     )

