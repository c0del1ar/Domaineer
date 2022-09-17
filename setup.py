#!/usr/bin/env python

import os, sys, re
from setuptools import setup, find_packages

with open('README.md', 'rb') as f:
    long_desc = f.read().decode("utf-8")

version = re.search(
    r'^os.environ\[\"version"\]\s*=\s*"(.*)"',
    open('src/domaineer/set_env.py').read(),
    re.M
).group(1)

install_req = ['bs4','requests']

if sys.platform.startswith("win"):
    install_req += ["colorama>=0.4.0"]

try:
    setup(
        name="domaineer",
        packages=find_packages(where="src"),
        package_dir={'domaineer': 'src/domaineer'},
        entry_points={
            'console_scripts': [
                'domaineer = domaineer.domaineer:main',
            ]
        },
        install_requires=install_req,
        include_package_data=True,
        version=version,
        description="Domaineer - An Auto Exploitation App",
        long_description=long_desc,
        long_description_content_type='text/markdown',
        author="Arya Kresna / @c0del1ar",
        author_email="aryakrishna436@gmail.com",
        url="https://kulihacker.com",
        license="GPLv3",
        python_requires=">=3.4",
        classifiers=[
            'Development Status :: 4 - Beta',
            'Natural Language :: English',
            'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
            'Programming Language :: Python',
            'Programming Language :: Python :: 3',
            'Programming Language :: Python :: 3.4',
            'Programming Language :: Python :: 3.5',
            'Programming Language :: Python :: 3.6',
            'Programming Language :: Python :: 3.7',
            'Programming Language :: Python :: 3.8',
            'Programming Language :: Python :: 3.9',
            'Programming Language :: Python :: 3.10',
        ],
        zip_safe=False,
    )
finally:
    pass
