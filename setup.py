from setuptools import setup, find_packages

setup (
       name='franceioi',
       version='0.1',
       packages=find_packages(),

       # Declare your packages' dependencies here, for eg:
       install_requires=['foo>=3'],
       # Fill in these to make your Egg ready for upload to
       # PyPI
       author='Amine M. Boulouma',
       author_email='amine@boulouma.com',

       #summary = 'Just another Python package for the cheese shop',
       url='http://amine.boulouma.com',
       license='',
       long_description='Long description of the package',

       # could also include long_description, download_url, classifiers, etc.

  
       )