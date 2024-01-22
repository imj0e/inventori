from setuptools import setup

setup(
    name='latihan_kasir',
    version='0.1',
    packages=['src'],
    entry_points={
        'console_scripts': [
            'latihan-kasir=src.main:main',
        ],
    },
)
