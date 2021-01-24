from setuptools import setup

setup(
    name='cvutils',
    version='0.1',
    packages=[''],
    url='',
    license='beer',
    author='patrick ryan',
    author_email='theyoungsoul@gmail.com',
    description='cvutil - collection of random utilities for computer vision',
    install_requires = [
        'opencv-python',
        'opencv-contrib-python',
        'json-minify',
        'imutils',
        'dropbox',
        'numpy',
        'beautifulsoup4'
    ]
)

