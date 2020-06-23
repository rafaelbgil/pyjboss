import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pyjboss", # Replace with your own username
    version="0.0.1",
    license="GNU General Public License v3.0",
    author="Rafael Benites Gil",
    author_email="rafaelbgil@gmail.com",
    description="Python client for Jboss and Wildfly api",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pypa/sampleproject",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=2.7',
)
