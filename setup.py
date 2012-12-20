import os
from setuptools import setup

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()
    
setup(
    name = 'tugboat',
    version = '0.1',
    author = 'Victor Watkins',
    author_email = 'vic.watkins@rackspace.com',
    description = ('A continuous integration/continuous delivery tool to log '
                   'into puppetmasters and agents to run config updates after '
                   'an automated deploy with another tool such as Flagship.'),
    license = '',
    keywords = 'ci cd continuous integration delivery puppet config',
    url = 'http://github.com/vickleford/tugboat',
    packages=['tugboat'],
    long_description=read('README'),
    classifiers=[],
)