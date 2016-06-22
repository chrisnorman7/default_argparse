from setuptools import setup, find_packages

setup(
 name = 'default_argparse',
 version = '0.0.0',
 description = 'My default argument parser.',
 url = 'http://github.com/chrisnorman7/default_argparse.git',
 author = 'Chris Norman',
 author_email = 'chris.norman2@googlemail.com',
 license = 'MPL',
 packages = find_packages(),
 zip_safe = False,
 long_description_markdown_filename = 'README.md',
 setup_requires = ['setuptools-markdown'],
)
