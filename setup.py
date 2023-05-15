from setuptools import setup, find_packages

# Add install requirements
setup(
    author="Anahit Zakaryan",
    description="A package for Bass model function.",
    name="mynewbassmodel",
    packages=['mynewbassmodel'],
    version="0.1.0",
    install_requires=['numpy>=1.10', 'pandas','matplotlib.pyplot','math','scipy.optimize'],
)
