from setuptools import setup

setup(
    name="Mudball",
    version="1.0.0",
    description="Tarball, but made by a ten year old",
    long_description=open('README','r'),
    long_description_content_type="text/markdown",
    url="https://github.com/realpython/reader",
    author="Donnie (Jack) Baldyga",
    author_email="jack@jackedac.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
    ],
    packages=["reader"],
    include_package_data=True,
    install_requires=[],
    entry_points={"console_scripts": ["Mud=Mudball.__main__:main"]},
)
