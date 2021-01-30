#!/usr/bin/env python

from setuptools import setup

setup(name='tap-zendesk',
      version='1.5.3',
      description='Singer.io tap for extracting data from the Zendesk API',
      author='Stitch',
      url='https://singer.io',
      classifiers=['Programming Language :: Python :: 3 :: Only'],
      py_modules=['tap_zendesk'],
      install_requires=[
          'singer-python @ git+ssh://git@github.com/hz-lschick/singer-python.git', #==5.9.0',
          'zenpy==2.0.23',
          'pytz==2018.9',
      ],
      dependency_links=[
          'git+ssh://git@github.com/hz-lschick/singer-python.git#egg=singer-python-5.9.0', # ==5.9.0 + not enforce specific version of pytz package
      ],
      extras_require={
          'dev': [
              'ipdb',
              'pylint',
              'nose',
              'nose-watch',
          ]
      },
      entry_points='''
          [console_scripts]
          tap-zendesk=tap_zendesk:main
      ''',
      packages=['tap_zendesk'],
      include_package_data=True,
)
