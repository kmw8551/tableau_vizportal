from setuptools import setup, find_packages

setup(
    name='tab_vizportal',
    version='1.0.0',
    description="Access and get data using Tableau Vizportal",
    author='Min Woong, Kang',
    author_email="kmw8551@naver.com",
    packages=find_packages(include=['server', 'server.*']),
    install_requires=[
        'pandas',
        'requests',
        'pycryptodome',
        'urllib'
    ],


    classifiers=[
            "Programming Language :: Python :: 3",
            "License :: OSI Approved :: MIT License",
            "Operating System :: OS Independent",
        ],

    python_requires='>=3.6',
)