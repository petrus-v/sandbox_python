from setuptools import setup, find_packages


setup(
    name="sandbox",
    version="1.0",
    author="Cyriac Pinto",
    author_email="cycy@gmail.com",
    url="https://github.com/cycy/sandbox",
    license="AGPL v3",
    description="Mes débuts en python",
    long_description=open('README.rst').read() + '\n'
        + open('CHANGES.rst').read(),
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "sandbox-app = utils:main",
        ],
    },
    install_requires=[
    ],
    tests_require=[
        'nose'
    ],
    test_suite='test',
    classifiers=[
        "Programming Language :: Python :: 3",
        "Intended Audience :: System Administrators",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: POSIX :: Linux",
        "Topic :: System :: Clustering",
        ],
)
