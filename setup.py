from setuptools import setup, find_packages

setup(
    name='wurstball-rss',
    version='0.1.1',
    packages=find_packages(".", exclude=["*.tests", "*.tests.*", "tests.*", "tests", "demo.*"]),
    scripts=['wurstball_rss'],
    url='https://github.com/olisim/wurstball-rss/',
    license='MIT',
    author='Oliver Simon',
    author_email='simon@dajool.com',
    maintainer='Jochen Breuer',
    maintainer_email='breuer@dajool.com',
    install_requires=['lxml', 'requests', 'pytz', 'feedgen'],
    description='A RSS feed generator for the front page of http://wurstball.de.',
    keywords='wurstball rss fun',
    platforms='any',
)
