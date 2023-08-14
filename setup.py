from setuptools import setup, find_packages
import os

VERSION = '0.0.9'
DESCRIPTION = 'Trainable, efficient, autonomous routing.'
LONG_DESCRIPTION = 'Trainable, efficient, autonomous routing for data flowing through LLMs'

setup(
    name="TeaRoute",
    version=VERSION,
    author="kesile",
    author_email="johncolekessler@gmail.com",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=['openai', 'numpy'],
    keywords=['python', 'ai', 'openai', 'chatgpt', 'routing', 'route'],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)