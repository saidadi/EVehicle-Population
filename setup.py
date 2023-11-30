from setuptools import setup, find_packages

setup(
    name='E-Vehicle-Population-Data-Analysis',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'matplotlib>=3.0.2',
        'numpy>=1.15.2',
        'pandas>=0.23.4',
        'seaborn>=0.11.0'
    ],
)
