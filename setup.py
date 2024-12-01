from setuptools import setup, find_packages

setup(
    name='ebrandom',
    version='0.0.1',
    packages=find_packages(),
    package_data={
        'linear_congruential': ['libLinearCongruential.so'],
        'mersenne_twister': ['libMersenneTwister.so'],
        'mid_square': ['libMidSquare.so']
    },
    include_package_data=True,
    description='A package containing various random number generators',
    install_requires=[],
)
