from setuptools import setup, find_packages

setup(
    name = 'siwp2005-vincentkarunia-sort',
    version = '0.0.2',
    packages=find_packages(),
    author = 'Vincent Karunia Pratama Simanjuntak',
    author_email = 'vincent.422023012@civitas.ukrida.ac.id',
    description = 'HW3 OOP',
    long_description = open('README.md').read(),
    long_description_content_type = 'text/markdown',
    url = 'https://github.com/vinckarunia/SIWP2005_OOP_HW3',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
