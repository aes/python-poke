#!/usr/bin/env python

import setuptools

setuptools.setup(
    name='poke',
    version='0.1.0',
    description='Basic (unsafe) peek and poke procedures for CPython',
    author='Anders Eurenius',
    author_email='aes@nerdshack.com',
    license='bsd',
    classifiers=[
        'Programming Language :: Python',
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Artistic License',
        'Operating System :: OS Independent'],
    url='https://github.com/aes/python-poke',
    ext_modules=[setuptools.Extension('poke', ['poke.c'])],
    test_suite="poke_test",
    )
