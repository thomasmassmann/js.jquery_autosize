from setuptools import setup, find_packages
import os

version = '1.18.13'


def read(*rnames):
    return open(os.path.join(os.path.dirname(__file__), *rnames)).read()

long_description = (
    read('README.txt')
    + '\n' +
    read('js', 'jquery_autosize', 'test_jquery_autosize.txt')
    + '\n' +
    read('CHANGES.txt'))

setup(
    name='js.jquery_autosize',
    version=version,
    description="fanstatic jQuery autosize.",
    long_description=long_description,
    classifiers=[],
    keywords='',
    author='Thomas Massmann',
    author_email='thomas.massmann@it-spir.it',
    url='https://bitbucket.org/it_spirit/js.jquery_autosize',
    download_url='http://pypi.python.org/pypi/js.jquery_autosize',
    license='BSD',
    packages=find_packages(),
    namespace_packages=['js'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'fanstatic',
        'js.jquery',
        'setuptools',
    ],
    entry_points={
        'fanstatic.libraries': [
            'jquery_autosize = js.jquery_autosize:library',
        ],
    },
)
