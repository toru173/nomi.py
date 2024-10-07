from setuptools import setup, find_packages

setup(
    name='nomi',
    author='toru173 Name',
    description='A Python module for interacting with the Nomi API',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/toru173/nomi.py',
    packages=find_packages(),
    python_requires='>=3.7',
)