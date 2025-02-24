#!/usr/bin/env python

from setuptools import setup

setup(
    name="curieconf_utils",
    version="1.0",
    description="Curiefense configuration utils",
    author="Reblaze",
    author_email="phil@reblaze.com",
    packages=["curieconf.utils"],
    install_requires=[
        "wheel",
        "google-crc32c==1.1.2",
        "minio==6.0.2",
        "cloudstorage [amazon, google, local, minio]==0.10.1",
        "pydash==5.0.2",
        "flask==1.1.2",
        "flask-restplus==0.13.0",
        "werkzeug==0.16.1",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ],
)
