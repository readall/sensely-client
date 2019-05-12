import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="sensely-client",
    version="0.0.1",
    author="Sensely.in",
    author_email="mail@sensely.in",
    description="A library to send data stream for ingestion and analytics",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/readall/sensely-client",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: properietary",
        "Operating System :: Linux",
    ]
)
