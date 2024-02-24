from setuptools import setup, find_packages

setup(
    name="mypackage",
    version="0.1",
    packages=find_packages(exclude=["test*"]),
    license="MIT",
    description="EDSA example python package",
    long_description=open("README.md").read(),
    install_requires=["numpy"],
    url="https://github.com/BlvckSanek/mypackage",
    author="Sanek Nelson",
    author_email="arkohnelsonemmanuel@gmail.com"
)