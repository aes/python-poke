#!/usr/bin/env python

import setuptools

setuptools.setup(
    name='poke',
    version='0.1.0',
    description='Z',
    author='Anders Eurenius',
    author_email='aes@nerdshack.com',
    license='bsd',
    # url='http://www.python.org/sigs/distutils-sig/',
    ext_modules=[setuptools.Extension('poke', ['poke.c'])],
    classifiers=[
        'Programming Language :: Python',
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent'])
