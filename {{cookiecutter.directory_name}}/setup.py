#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

with open("README.rst") as readme_file:
    readme = readme_file.read()

requirements = []

test_requirements = ["pytest>=3", ]

setup(
    author="""{{cookiecutter.author}}""",
    author_email="{{cookiecutter.email}}",
    python_requires=">=3.6",
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
    ],
    description="""{{cookiecutter.system_description}}""",
    install_requires=requirements,
    long_description=readme,
    include_package_data=True,
    keywords="{{cookiecutter.system_name}}",
    name="{{cookiecutter.system_name}}",
    packages=find_packages(include=["{{cookiecutter.system_name}}", "{{cookiecutter.system_name}}.*"]),
    test_suite="tests",
    tests_require=test_requirements,
    version="0.1.0",
    zip_safe=False,
)
