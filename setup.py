from setuptools import setup
from VERSION import __version__

with open('README.rst') as readme:
    long_description = readme.read()

setup(name='colorit',
    version=__version__,
    description='A RGB format coloring for terminal',
    long_description=long_description,
    url='https://gihub.com/arjunsinghy96/colorit',
    author='Arjun Singh Yadav',
    author_email='14bcs010@smvdu.ac.in',
    license='MIT',
    keywords='color terminal RGB',
    classifiers=[
        'Development Status :: 3-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5'
        ],
    py_modules=['colorit']
    )
