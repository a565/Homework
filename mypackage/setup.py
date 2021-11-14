from setuptools import setup

setup(
    name='work',
    version='1.0',
    author='Author',
    packages=['work'],
    description='Description',
    package_data={'': ['*.txt']},
    install_requires=['requests'],
    entry_points={'console_scripts': ['work = work:main']},
)
