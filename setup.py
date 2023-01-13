from setuptools import setup, find_packages
from os import path

this_directory = path.abspath(path.dirname(__file__))

# imports from __version__
with open(path.join(this_directory, 'pyECSS', '_version.py'), encoding='utf-8') as f:
    exec(f.read())

with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='pyECSS',
    version=__version__, 
    license='Apache 2', 
    description = "pyECSS (Entity Component Systems in a Scenegraph)",
    long_description=long_description,
    # long_description= file: README.md, LICENSE.txt
    long_description_content_type='text/markdown',
    author = "George Papagiannakis", 
    author_email = "papagian@csd.uoc.gr",
    maintainer='Manos Kamarianakis',
    maintainer_email='m.kamarianakis@gmail.com',
    url='https://github.com/papagiannakis/pyECSS',
    keywords = ['ECS','Scenegraph','Python design patterns','Computer Graphics'],
    package_dir={'pyECSS':'pyECSS'},
    packages=find_packages(exclude=["tests","tests.*", "tests/*" ]),
    install_requires=[
        'pip',
        'setuptools>=61',
        'wheel', 
        'numpy', 
        'scipy',
    ],
    

    classifiers=[
        "License :: OSI Approved :: Apache Software License",
        "Environment :: MacOS X",
        "Environment :: Win32 (MS Windows)",
        "Environment :: X11 Applications",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: MacOS",
        "Operating System :: Unix",
        "Programming Language :: Python :: 3.9",
    ],
    project_urls={
        "Homepage" : "https://github.com/papagiannakis/pyECSS",
        "Documentation" : "https://pyecss.readthedocs.io",
        "Bug Tracker": "https://github.com/papagiannakis/pyECSS",
        "Source Code": "https://github.com/papagiannakis/pyECSS",
    },

    python_requires=">=3.8,<3.10",
)