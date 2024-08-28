from setuptools import setup, find_packages

setup(
    name='ZAL-FUZZER',
    version='0.1',
    description='ZAL-FUZZER is a python based web fuzzer designed to help web pentesters automate the discovery of endpoints/paths contained in a web application',
    author='David',
    author_email='zalparus22@gmail.com',
    packages=find_packages(),
    install_requires=[
       'argparse',
       'logging',
        'json'
    ],
    entry_points={
        'console_scripts': [
            'my_script=main.py',
        ],
    },
)

