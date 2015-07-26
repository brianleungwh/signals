import os
from setuptools import setup, find_packages


def read(filename):
    with open(os.path.join(os.path.dirname(__file__), filename), 'r') as f:
        return f.read()

long_description = "{}\n\n{}".format(read("README.rst"),
                                     read("CONTRIBUTORS.rst"))

setup(
    name="yak-signals",
    packages=find_packages(exclude=["tests*"]),
    version="0.2.1",
    description="A tool for auto generating libraries for different platforms to communicate with your API",
    long_description=long_description,
    url="https://github.com/yeti/signals/",
    license="MIT",
    author="Rudy Mutter",
    author_email="support@yeti.co",
    install_requires=[
        "click>=4.0",
        "lxml>=3.4",
        "Jinja2>=2.7.3"
    ],
    entry_points={
        "console_scripts": [
            "signals=signals.main:main"
        ]
    },
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Topic :: Software Development",
        "Topic :: Software Development :: Build Tools",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ]
)