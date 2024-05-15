from setuptools import setup, find_packages

setup(
    name='ops',
    version='1.0.0',
    author='Vismaya',
    description='A simple calculator application',
    packages=find_packages(),
    python_requires='>=3.6',
    install_requires=[
        # Add any dependencies here
    ],
    entry_points={
        'console_scripts': [
            'ops = calculator.calculator:main'
        ]
    }
)
