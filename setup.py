#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

with open('README.md') as readme_file:
    readme = readme_file.read()

setup(
    author="Sam Dobson",
    author_email='1309834+samdobson@users.noreply.github.com',
    python_requires='>=3.5',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    description="Component for displaying important figures on a Streamlit dashboard",
    install_requires=['streamlit>=0.68'],
    license="MIT license",
    long_description=readme,
    long_description_content_type='text/markdown',
    keywords='streamlit',
    name='streamlit_metrics',
    packages=find_packages(),
    url='https://github.com/samdobson/streamlit_metrics',
    version='0.1.0',
    zip_safe=False,
)
