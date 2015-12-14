from setuptools import setup
import pysls

setup(
    name='pysls',
    version=pysls.__version__,
    author=pysls.__author__,
    description=pysls.__description__,
    author_email=pysls.__email__,
    url='https://github.com/k0st1an/pysls',
    packages=['pysls'],
    install_requires=['redis>=2.10.5'],
    license='MIT'
)
