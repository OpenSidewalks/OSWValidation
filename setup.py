from setuptools import find_packages, setup

setup(
    name='OSWValidation',
    packages=find_packages(include=['OSWValidation']),
    version='0.1.0',
    description='Python functions for validating OSW data',
    author='yehe@cs.washington.edu',
    install_requires=[],
    setup_requires=['pytest-runner'],
    tests_require=['pytest'],
    test_suite='tests'
)