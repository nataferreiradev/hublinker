from setuptools import setup, find_packages

setup(
    name='hublinker',
    version='0.1.0',
    packages=find_packages(),
    include_package_data=True,
    entry_points={
        'console_scripts': [
            'hublinker=hublinker.cli:main',  
        ],
    },
    description='hublinker: A CLI tool for interacting with the GitHub API directly from the terminal, making listings, cloning, and more easy',
    license='MIT',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
