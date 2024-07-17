from setuptools import setup, find_packages

setup(
    name='face-reco',
    version='1.0.0',
    packages=find_packages(),
    install_requires=[
        'flask',
        'sqlalchemy',
        'pymongo',
        'redis',
        'passlib',
        'requests',
    ],
    entry_points={
        'console_scripts': [
            'face-reco=src.app:main',
        ],
    },
)
