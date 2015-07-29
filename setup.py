from sys import version_info
import os
# Prevent spurious errors during `python setup.py test` in 2.6, a la
# http://www.eby-sarna.com/pipermail/peak/2010-May/003357.html:
try:
    import multiprocessing
    # silence pyflakes
    assert multiprocessing
except ImportError:
    pass

from setuptools import setup, find_packages

def read(fname):
        return open(os.path.join(os.path.dirname(__file__), fname)).read()
setup(
    name='erl_terms',
    version='0.1.1',
    description='Erlang term read library',
    long_description=read('README'),
    author='Machine Zone',
    author_email='info@machinezone.com',
    license='proprietary',
    packages=find_packages(exclude=['ez_setup']),
    install_requires=['parsimonious'],
    tests_require=['nose'],
    test_suite='nose.collector',
    url='https://github.com/machinezone/python_etf',
    include_package_data=True,
    classifiers=[
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Development Status :: 2 - Pre-Alpha',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.1',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Topic :: Software Development :: Libraries',
        'Topic :: Text Processing :: General'],
    keywords=['parse', 'parser', 'erlang', 'peg', 'grammar', 'language'],
    use_2to3=version_info >= (3,)
)
