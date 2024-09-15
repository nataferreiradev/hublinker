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
    author='Seu Nome',
    description='hublinker: A CLI tool for interacting with the GitHub API directly from the terminal, making listings, cloning, and more easy',
    url='https://github.com/seuusuario/hublinker',
    license='MIT',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
