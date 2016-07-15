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
    classifiers=[
        'Development Status :: 4 - Beta',

        # Indicate who your project is intended for
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries :: Python Modules',

        # Pick your license as you wish (should match "license" above)
        'License :: OSI Approved :: MIT License',

        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
    ],
    keywords = ['spice', 'MyAnimeList', 'API'], # arbitrary keywords
    install_requires = ['requests', 'lxml', 'beautifulsoup4'],
)
