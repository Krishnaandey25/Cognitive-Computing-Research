from setuptools import setup, find_packages

setup(
    name="cognitive_computing_research",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "networkx",
        "scipy",
        "numpy",
        "torch",
    ],
    author="Krishna Pandey",
    description="Advanced Cognitive Computing & Neural-Symbolic Research",
)