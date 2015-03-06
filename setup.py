from setuptools import setup
import sys

install_requires = []
if sys.version_info < (2, 6):
    install_requires.append("simplejson >= 3.3.0")

setup(
    name='pydruid',
    version='0.2.0',
    author='Deep Ganguli',
    author_email='deep@metamarkets.com',
    packages=['pydruid', 'pydruid.utils'],
    url='http://pypi.python.org/pypi/pydruid/',
    license='LICENSE',
    description='A Python connector for Druid.',
    long_description='See https://github.com/metamx/pydruid for more information.',
    install_requires=install_requires
)

