from distutils.core import setup
setup(
    name = 'spice',
    packages = ['spice'], # this must be the same as the name above
    version = '0.0.1dev',
    description = 'spice - testing',
    long_description = open('README.md').read(),
    license = 'MIT',
    author = 'Mehrab Hoque',
    author_email = 'mehrabhoque@gmail.com',
    url = 'https://github.com/Utagai/spice', # use the URL to the github repo
    keywords = ['spice', 'MyAnimeList', 'API'], # arbitrary keywords
    install_requires = ['requests', 'lxml', 'beautifulsoup4'],
)
