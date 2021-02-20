import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="letter-tools",
    version="0.2.3",
    author="Hostedposted",
    author_email="hostedpostedsite@gmail.com",
    description="Python tools for doing stuff with letters.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/hostedposted/letter-tools",
    packages=setuptools.find_packages(exclude="/words.json"),
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        "requests>=2.25.0"
    ],
    python_requires='>=2.7',
)