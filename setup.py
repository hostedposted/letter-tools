import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="letter-tools",
    version="0.0.3",
    author="Hostedposted",
    author_email="hostedpostedsite@gmail.com",
    description="Python tools for doing stuff with letters.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/hostedposted/letter-tools",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)