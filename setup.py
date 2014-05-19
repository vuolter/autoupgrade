# coding=utf-8

from distutils.core import setup
#from setuptools import setup

__version__ = "unknown"
exec(open('autoupgrade/version.py').read())
print "autoupgrade version: " + __version__

setup(name='autoupgrade',
      version=__version__,
      author= 'Jörgen Karlsson',
      author_email='jorgen@karlsson.com',
      license='MIT',
      description='Automatic upgrade of python modules and packages',
      long_description=open('README.txt').read(),
      packages=['autoupgrade'],
      url = "https://bitbucket.org/jorkar/autoupgrade",
      install_requires = ["BeautifulSoup4"])
