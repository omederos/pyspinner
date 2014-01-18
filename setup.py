from distutils.core import setup
import spinning

setup(
    name='PySpinner',
    version=spinning.__version__,
    description='A simple spin-syntax parser for Python',
    author='Oscar Mederos',
    author_email='omederos@gmail.com',
    url='http://github.com/omederos/pyspinner',
    packages=['spinning',],
    license='MIT License',
    long_description=open('README.txt').read(),
)